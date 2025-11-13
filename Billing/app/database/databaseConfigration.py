import mysql.connector
from mysql.connector.errors import Error

def ConnectionClose(connection):
    if connection and connection.is_connected():
        connection.close()
        print("connection closed")
    

def create_database():
    connection = None

    try:
        connection =mysql.connector.connect(host='localhost', user='root', password='Pandian@1707')

        if connection.is_connected():
            cursor = connection.cursor()
            database_name = 'Billing_app'   
            cursor.execute(
            f"CREATE DATABASE IF NOT EXISTS {database_name} ")

            cursor.execute(
                f"USE {database_name}"  
                )
            print(F'${database_name} has used')
            cursor.execute(
                """
                CREATE TABLE IF NOT EXISTS product(
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    name VARCHAR(255) NOT NULL ,
                    price INT NOT NULL ,
                    gst_percent INT NOT NULL ,
                    stock INT ,
                    sku VARCHAR(255) NOT NULL
                )
                """
            )
            print("Database Created Successfully")

            cursor.execute(
                """
                CREATE TABLE IF NOT EXISTS invoices(
                    ID INT AUTO_INCREMENT PRIMARY KEY,
                    INVOICE_NUMBER TEXT  ,
                    DATE DATETIME NOT NULL ,
                    CUSTOMER_NAME TEXT NOT NULL ,
                    PHONE TEXT ,
                    TOTAL_AMOUNT NUMERIC NOT NULL ,
                    GST_AMOUNT NUMERIC NOT NULL ,
                    GRAND_TOTAL NUMERIC NOT NULL
                )    
                """
            )

            cursor.execute(
                """
                CREATE TABLE IF NOT EXISTS invoice_items(
                    ID INT AUTO_INCREMENT PRIMARY KEY,
                    INVOICE_ID INT,
                    FOREIGN KEY (INVOICE_ID) REFERENCES invoice(id),
                    PRODUCT_ID INT,
                    FOREIGN KEY (PRODUCT_ID) REFERENCES product(id),
                    QUANTITY INT NOT NULL ,
                    PRICE NUMERIC ,
                    GST_PERCENT NUMERIC NOT NULL ,
                    TOTAL NUMERIC NOT NULL 
                    
                )    
                """
            )   

            return connection

    except Error as e:
        print(f'Error occurs {e}')

    
if __name__ == "__main":
    db_connection = create_database           



