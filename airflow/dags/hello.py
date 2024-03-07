from airflow import DAG
from airflow.operators.dummy_operator import DummyOperator
from airflow.operators.python_operator import PythonOperator
from datetime import datetime, timedelta

# Define default_args dictionary to specify default parameters for the DAG
default_args = {
    'owner': 'airflow',
    'start_date': datetime(2024, 2, 15),
    'depends_on_past': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

# Instantiate the DAG with the defined default_args
dag = DAG(
    'airflow_etl_dag',
    default_args=default_args,
    description='A simple example DAG for ETL process',
    schedule_interval=timedelta(days=1),  # Run the DAG daily
)

# Define tasks in the workflow
start_task = DummyOperator(
    task_id='start',
    dag=dag,
)

# Python function that represents the Extract task
def extract_data():
    print("Extracting data")

extract_task = PythonOperator(
    task_id='extract_task',
    python_callable=extract_data,
    dag=dag,
)

# Python function that represents the Transform task
def transform_data():
    print("Transforming data")

transform_task = PythonOperator(
    task_id='transform_task',
    python_callable=transform_data,
    dag=dag,
)

# Python function that represents the Load task
def load_data():
    print("Loading data")

load_task = PythonOperator(
    task_id='load_task',
    python_callable=load_data,
    dag=dag,
)

end_task = DummyOperator(
    task_id='end',
    dag=dag,
)

# Define the task dependencies
start_task >> extract_task >> transform_task >> load_task >> end_task