import mysql.connector

try:
    connection = mysql.connector.connect(host="localhost", user="iann34", password="root67")
    database = "alx_book_store"
    cursor = connection.cursor()
    command = f"CREATE DATABASE {database}"

    cursor.execute(command)
    print(f"Database '{database}' created successfully!")
    cursor.close()
    connection.close()
except mysql.connector.errors.DatabaseError as error:
    print(error.msg)
