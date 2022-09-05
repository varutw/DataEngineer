# Airflow_with_Docker_Compose
This file explains the usage of Airflow with docker-compose

## Installation
Procedures for installing Airflow with Airflow with docker-compose can be found in [https://airflow.apache.org/docs/apache-airflow/stable/start/docker.html].

## Location of dag file
Also, any dedired modification must be done in the file in the mentioned directory, or the change will not take any effect.

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


