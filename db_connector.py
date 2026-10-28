import mysql.connector
from mysql.connector import Error

def connect_to_db():
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="root",
            database="kmk_krakow_etl"
        )
        if connection.is_connected():
            print("Success! You are connected to the MariaDB database.")
            return connection
    except Error as e:
        print(f"Error while connecting to the database: {e}")
        return None

if __name__ == "__main__":
    connect_to_db()



