import mysql.connector

database_connection = mysql.connector.connect(
	host="localhost",
	port=8889,
	user="root",
	password="root",
	database="SELECTION_DB"
)

connection_cursor = database_connection.cursor()
connection_cursor.execute(
	"ALTER TABLE EMP_SELECTION "
	"ADD ADDRESS VARCHAR(50)"
)

database_connection.close()
