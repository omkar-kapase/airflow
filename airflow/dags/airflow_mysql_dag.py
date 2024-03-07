import os
from datetime import datetime, timedelta,timezone
import mysql.connector
import time
 

 # MySQL connection details
 mysql_host = "	mysqlsrv09.mysql.database.azure.com"
 mysql_port = 3306
 mysql_username = "ashish"
 mysql_password = "Admin@789"
 mysql_database = "test"  # Specify your database name
 
 # Establish MySQL connection
 conn = mysql.connector.connect(
     host=mysql_host,
     port=mysql_port,
     user=mysql_username,
     password=mysql_password,
     database=mysql_database,
     ssl_disabled=True
 )
 cursor = conn.cursor()
                 sql = "INSERT INTO airflow.jobs (job_name) VALUES ( %s)"
                 val = ('Software Engineer', 'Data Analyst')
                 cursor.execute(sql, val)
                 conn.commit()