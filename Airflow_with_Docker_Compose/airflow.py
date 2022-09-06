from airflow.models import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator
from airflow.providers.google.cloud.transfers.gcs_to_bigquery import GCSToBigQueryOperator
from airflow.providers.google.cloud.operators.bigquery import BigQueryExecuteQueryOperator
from airflow.utils.dates import days_ago
import pandas as pd
import gdown

superstore_url = "https://drive.google.com/uc?id=1d3Ydv4B5ozb-FrsKQ2GZiZdGIqJg-kpa"
superstore_output_path = "/home/airflow/gcs/data/superstore.csv"

def get_superstore(input_link,output_path):
    gdown.download(input_link, output_path, quiet=False)

with DAG(
    "ever_medical_airflow",
    start_date=days_ago(1),
    schedule_interval="@once",
    tags=["assignment"]
) as dag:

    dag.doc_md = """
    This is an example of ETL process of using Apache Airflow in Google Cloud Composer. The steps would be:
    * Download Superstore dataset from Google Drive using gdown package as csv file and save to Google Cloud Storage (GCS) 
    * Load data from GCS to Google Big Query
    * Create view to find the longest duration
    
    """
    
    # task to download dataset into GCS
    t1 = PythonOperator(
        task_id="get_superstore_data",
        python_callable=get_superstore,
        op_kwargs={
            "input_link": superstore_url,
            "output_path": superstore_output_path,
        },
    )

    # task to load dataset into BigQuery
    t2 = BashOperator(
        task_id="GCS_to_BiqQuery",
        bash_command='bq load \
        --source_format=CSV --autodetect \
        ever_medial_de_dataset.ever_medial_de_table \
        gs://asia-southeast1-ever-medica-6f075862-bucket/data/superstore.csv'
        
    )

    # task to perform data cleansing and find the longest shipping duration
    t3 = BigQueryExecuteQueryOperator(
    task_id="create_view",
    sql="""
        with converted as (
     select *,
    safe.parse_date('%m/%d/%Y',replace(Order_Date,'2116','2016')) as new_order_date,
    safe.parse_date('%m/%d/%Y',replace(Ship_Date,'2055','2015')) as new_ship_date
    from `ever-medial-data-engineer.ever_medial_de_dataset.ever_medial_de_table`
    )
    select *,
    date_diff(new_ship_date,new_order_date,DAY) as duration
    from converted
    where new_ship_date>new_order_date
    order by duration desc
    limit 5
    """,
    destination_dataset_table=f"ever-medial-data-engineer.ever_medial_de_dataset.ever_medial_de_view",
    write_disposition="WRITE_TRUNCATE",
    use_legacy_sql=False
)

    # create dependencies
    t1 >> t2 >> t3
