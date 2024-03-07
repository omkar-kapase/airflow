from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from datetime import datetime

# Define your DAG
dag = DAG(
    'run_python_script',
    schedule_interval=None,  # or your desired schedule
    start_date=datetime(2024, 2, 23),  # or your desired start date
    catchup=False  # if you don't want historical runs to execute
)

# Define the task to run the Python script
run_python_script_task = BashOperator(
    task_id='run_python_script_task',
    bash_command='python airflow_dag.py',
    dag=dag
)

# Define the order of tasks
run_python_script_task