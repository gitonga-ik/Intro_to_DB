import mysql.connector
import os

host = os.environ.get("host")
user = os.environ.get("user")
password = os.environ.get("password")

try:
    connection = mysql.connector.connect(host=host, user=user, password=password)
    cursor = connection.cursor()
    command = "CREATE DATABASE IF NOT EXISTS alx_book_store"

    cursor.execute(command)
    print("Database 'alx_book_store' created successfully!")
    cursor.close()
    connection.close()
except mysql.connector.errors.DatabaseError as error:
    print(error.msg)
