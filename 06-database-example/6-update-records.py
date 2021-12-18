import mysql.connector

try:
	database_connection = mysql.connector.connect(
		host="localhost",
		port=8889,
		user="root",
		password="root",
		database="SELECTION_DB"
	)
	connection_cursor = database_connection.cursor()

	sql_statement = "UPDATE EMP_SELECTION SET AGE=AGE+1 WHERE GENDER='M'"

	connection_cursor.execute(sql_statement)

	database_connection.commit()
	print(connection_cursor.rowcount, "record(s) updated.")

except mysql.connector.Error as error:
	print("parameterized query failed {}".format(error))
finally:
	if database_connection.is_connected():
		connection_cursor.close()
		database_connection.close()
		print("MySQL connection is closed")
