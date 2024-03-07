from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
import mysql.connector
import logging

# MySQL connection details
mysql_host = "mysqlsrv09.mysql.database.azure.com"
mysql_port = 3306
mysql_username = "ashish"
mysql_password = "Admin@789"
mysql_database = "test"  # Specify your database name

# Define the DAG
default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2024, 2, 26),
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

dag = DAG(
    'airflow_insert_jobs_dag',
    default_args=default_args,
    description='A DAG to insert jobs into MySQL',
    schedule_interval=None,  # Set your desired schedule
)

# Function to execute the MySQL query
def execute_mysql_query():
    try:
        connection = mysql.connector.connect(
            host=mysql_host,
            port=mysql_port,
            user=mysql_username,
            password=mysql_password,
            database=mysql_database
        )

        with connection.cursor() as cursor:
            insert_query = """
                INSERT INTO airflow.jobs (job_name) VALUES
                ('Software Engineer'),
                ('Data Analyst'),
                ('Project Manager'),
                ('Graphic Designer');
            """
            cursor.execute(insert_query)

        connection.commit()
    except Exception as e:
        logging.error(f"Error while executing MySQL query: {str(e)}")
    finally:
        connection.close()

# Define the PythonOperator task
insert_jobs_task = PythonOperator(
    task_id='insert_jobs_task',
    python_callable=execute_mysql_query,
    dag=dag,
)

# Additional tasks
task_before_insert = PythonOperator(
    task_id='task_before_insert',
    python_callable=lambda: logging.info("This task runs before inserting jobs."),
    dag=dag,
)

task_after_insert = PythonOperator(
    task_id='task_after_insert',
    python_callable=lambda: logging.info("This task runs after inserting jobs."),
    dag=dag,
)

# Set task dependencies
task_before_insert >> insert_jobs_task
insert_jobs_task >> task_after_insert

if __name__ == "__main__":
    dag.cli()
