import mysql.connector

database_connection = mysql.connector.connect(
	host="localhost",
	port=8889,
	user="root",
	password="root",
	database="SELECTION_DB"
)

print(database_connection)
