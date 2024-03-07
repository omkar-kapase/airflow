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
    values =(115, "cat"),
            
    cursor.execute(query, values)

    print('Values uploaded')

    # Commit the transaction and close the connection
    conn.commit()
    conn.close()

if __name__ == "__main__":
    execute_mysql_query()
