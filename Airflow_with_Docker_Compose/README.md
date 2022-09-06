# Airflow_with_Docker_Compose
This file explains the usage of Airflow with docker-compose, which is an interesting choice for low-cost data engineering.

Airflow is a data pipeline orchestration tool. Normally, I would prefer using Airflow with Google Cloud Composer. However, Cloud Composer can be really expensive and may be not suitable for small companies. Alternatively, Airflow can be hosted using Docker compose in a server, either on-premise or cloud services, such as AWS EC2 or Google Cloud Compute Engine. The advantage is that it greatly reduces the cost of using a fully managed data workflow orchestration service, such as Google Cloud Composer or Astronomer. The downside is that a data engineer must have some knowledge of using and maintaining Docker compose container.

## Installation
Procedures for installing Airflow with Airflow with docker-compose can be found in [https://airflow.apache.org/docs/apache-airflow/stable/start/docker.html]. In this case, Airflow is installed in '~'

## Location of dag file
Any dedired modification must be done in the dag file in the '~/airflow/dags/dags', or the change will not take any effect.

## Example DAGs
The example DAGs to demonstrate Airflow with Docker compose is in the file named 'airflow.py'. The dependencies are as following:

![image5](https://user-images.githubusercontent.com/45530179/188531314-f8cc1ba3-e7fe-41a6-b0d6-1c5311700537.png)

* __get_superstore_data__ Download Superstore dataset from Google drive link and save to Google Cloud Storage (GCS) bucket. 
* __GCS_to_BigQuery__ Load dataset from GCS to Google BigQuery. 
* __create_view__ Create BigQuery view to find the longest shipping duration. 

## Running Airflow
The Airflow dags can operate only if Airflow docker-compose is up. If it is not up, go to the airflow folder first.
```
cd ~/airflow
```
Make sure that 'docker-compose.yaml' and 'Dcokerfile' is in the directory. Then, type the command to start Airflow docker-compose.
```
docker-compose up
```

## Airflow UI Access

![Screenshot from 2022-09-05 14-40-33](https://user-images.githubusercontent.com/106131723/188395148-744ec19e-8e82-40cc-ba78-8cc37c3044e8.png)

## Adding more Python Packages
In case that more Python packages (modules) are required, please follow these steps:
1. Stop docker-compose
```
docker-compose down
```
2. Add the name of packages in 'requirement.txt'. The list of packages that are already installed also can be found in this file.
```
nano ~/airflow/requirement.txt
```
3. Build the new docker-compose image file with the same name
```
cd ~/airflow
docker build -t apache/airflow:2.2.3
```
4. Re-initialize the docker-compose
```
docker-compose up airflow-init
```

