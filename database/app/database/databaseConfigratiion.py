import mysql.connector
from mysql.connector.errors import Error

def connectionClose(connection):
     if connection and connection.is_connected():
            connection.close()
            print("connection closed") 


def create_database():
    connection = None 

    try: 
        connection = mysql.connector.connect(
            host='localhost',
            user= 'root',
            password='',
        )

        if connection.is_connected():
            cursor = connection.cursor()

            database_name = 'fastapi_crud'

            cursor.execute(
                f"CREATE DATABASE IF NOT EXISTS {database_name} "
            )

            cursor.execute(
                f"USE {database_name}"
            )
            print(f"${database_name} has used")
            cursor.execute(
     """
    CREATE TABLE IF NOT EXISTS user(
        id INT AUTO_INCREMENT PRIMARY KEY ,
        username VARCHAR(255) NOT NULL ,
        age INT NOT NULL ,
        email VARCHAR(255) NOT NULL
        )
    """
        )

            print("Database Created Sucessfully")
            return connection

    except Error as e:
        print(f'Error occurs {e}')

    if __name__ == "_main" :
         db_connection = create_database