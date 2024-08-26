import mysql.connector
import pandas as pd

def connect_to_database():
    try:
        connection = mysql.connector.connect(
            user='root',
            password='',  
            host='localhost',
            database='ecommerce'
        )

        if connection.is_connected():
            print("Connected to the database successfully")
        return connection

    except mysql.connector.Error as e:
        print("Error connecting to MySQL database:", e)
        return None

def fetch_data(connection):
    if connection is None:
        return None, None, None
    
    cursor = connection.cursor()
    
    # Fetch data from tables
    cursor.execute('SELECT * FROM customer')
    customer_data = pd.DataFrame(cursor.fetchall(), columns=[desc[0] for desc in cursor.description])

    cursor.execute('SELECT * FROM product')
    product_data = pd.DataFrame(cursor.fetchall(), columns=[desc[0] for desc in cursor.description])

    cursor.execute('SELECT * FROM order_details')
    order_data = pd.DataFrame(cursor.fetchall(), columns=[desc[0] for desc in cursor.description])

    cursor.close()
    return customer_data, product_data, order_data
