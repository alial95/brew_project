import pymysql


def read_database_people(list_name):
    connection = pymysql.connect(
		"localhost",
		"root",
		"barnformtreefred",
		"ali_test"
	)
    cursor = connection.cursor()
    cursor.execute("SELECT person_id, person_name, age FROM person")
    rows = cursor.fetchall()
    for row in rows:
        person = Person(row[1], row[2])
        list_name.append(person)
    cursor.close()
    connection.close()
    return list_name

def read_database_drinks(list_name):
    connection = pymysql.connect(
		"localhost",
		"root",
		"barnformtreefred",
		"ali_test"
	)
    cursor = connection.cursor()
    cursor.execute("SELECT drink_id, drink_name, container, volume FROM drinks")
    rows = cursor.fetchall()
    for row in rows:
        drink = Drink(row[1], row[2], row[3])
        list_name.append(drink)
    cursor.close()
    connection.close()
    return list_name
