from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime
from mysql_script import execute_mysql_query

# Define your MySQL connection string ID
mysql_conn_id = 'mysql_conn'


# Define your DAG
dag = DAG(
    'mysql_insert_dag',
    description='A DAG to insert values into MySQL table',
    schedule_interval=None,
    start_date=datetime(2024, 2, 28),
    catchup=False
)

# Define a task using PythonOperator and link it to your Python function
mysql_insert_task = PythonOperator(
    task_id='mysql_insert_task',
    python_callable=execute_mysql_query,
    dag=dag,
    retries=3
)

#root@ubuntugui:~/airflow/dags# cat mysql_script.py
import mysql.connector

def execute_mysql_query():
    # Connect to MySQL
    conn = mysql.connector.connect(
        host="mysqlsrv09.mysql.database.azure.com",
        user="ashish",
        password="Admin@789",
        database="airflow"
    )
    cursor = conn.cursor()

    # Insert values into the table
    query = "INSERT INTO testing (job_id, job_name) VALUES (%s, %s)"
    values =
            (103, "dog")
    cursor.execute(query, values)

    print('Values uploaded')

    # Commit the transaction and close the connection
    conn.commit()
    conn.close()

if __name__ == "__main__":
    execute_mysql_query()
