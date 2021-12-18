import mysql.connector

database_connection = mysql.connector.connect(
	host="localhost",
	port=8889,
	user="root",
	password="root"
)

connection_cursor = database_connection.cursor()
connection_cursor.execute("CREATE DATABASE SELECTION_DB")
database_connection.close()
