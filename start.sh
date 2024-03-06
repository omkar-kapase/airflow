#!/bin/bash


# Initialize the database migrations
airflow db init

# Create an admin user
airflow users create \
  --username omkar \
  --password omkar@123 \
  --firstname omkar \
  --lastname kapase \
  --role Admin \
  --email omkarkapase242@gmail.com

airflow webserver --port 8080

airflow scheduler

