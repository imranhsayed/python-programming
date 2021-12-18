import mysql.connector

database_connection = mysql.connector.connect(
	host="localhost",
	port=8889,
	user="root",
	password="root",
	database="SELECTION_DB"
)
connection_cursor = database_connection.cursor()

sql_statement = """INSERT INTO EMP_SELECTION (FIRST_NAME, LAST_NAME, AGE, GENDER, INCOME, ADDRESS) VALUES (%s, %s, 
%s, %s, %s, %s)"""
values = [
	("John", "Doe", 24, "M", 2400, "123 ABC Farm"),
	("Imran", "Sayed", 14, "M", 1400, "213 ABC Farm"),
	("Sony", "Rajan", 13, "F", 1000, "218 ABC Farm"),
]
connection_cursor.executemany(sql_statement, values)

database_connection.commit()
print(connection_cursor.rowcount, "was inserted.")

database_connection.close()
