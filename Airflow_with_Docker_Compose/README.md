# Airflow_with_Docker_Compose
This file explains the usage of Airflow with docker-compose.

Airflow is a data pipeline orchestration tool. Normally, I would prefer using Airflow with Google Cloud Composer. However, Cloud Composer can be really expensive and may be not suitable for small companies. Alternatively, Airflow can be hosted using Docker compose in a server, either on-premise or cloud services, such as AWS EC2 or Google Cloud Compute Engine. 

## Installation
Procedures for installing Airflow with Airflow with docker-compose can be found in [https://airflow.apache.org/docs/apache-airflow/stable/start/docker.html]. In this case, Airflow is installed in '~'

## Location of dag file
Any dedired modification must be done in the dag file in the '~/airflow/dags/dags', or the change will not take any effect.

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


