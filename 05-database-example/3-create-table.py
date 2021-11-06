import mysql.connector

database_connection = mysql.connector.connect(host="localhost", port=8889, user="root", password="root",
											  database="SELECTION_DB")

connection_cursor = database_connection.cursor()
connection_cursor.execute(
	"CREATE TABLE EMP_SELECTION ("
	"FIRST_NAME VARCHAR(15) NOT NULL,"
	"LAST_NAME VARCHAR(15) NOT NULL,"
	"AGE INT NOT NULL,"
	"GENDER VARCHAR(10) NOT NULL,"
	"INCOME INT NOT NULL"
	")")

database_connection.close()
