import pymysql 


def main():
	connection = pymysql.connect(
		"localhost",
		"root",
		"barnformtreefred",
		"mysql"
	)
	cursor = connection.cursor()
	cursor.execute("SELECT person_id, first_name FROM person")
	rows = cursor.fetchall()
	for row in rows:
		print("ID - " + str(row[0]) + ", Name - " + row[1])
	cursor.close()
	connection.close()

main()
