import pymysql
people_list = []

class Person:
    def __init__(self, name, age):
        """Get the human's name and age."""
        self.name = name
        self.age = age
    def __repr__(self):
        return f'{self.name}, {self.age}'


class Drink:
    def __init__(self, drink_name, container, volume):
        self.drink_name = drink_name
        self.container = container
        self.volume = int(volume)

    def have_drink(self, volume_poured):
        self.volume -= volume_poured

    def __repr__(self):
        return (f"{self.drink_name}, {self.container}, {self.volume}")

def read_database_people(list_name):
    connection = pymysql.connect(
		"localhost",
		"root",
		"barnformtreefred",
		"ali_test"
	)
    cursor = connection.cursor()
    cursor.execute("SELECT person_id, first_name, age FROM person")
    rows = cursor.fetchall()
    for row in rows:
        person = Person(row[1], row[2])
        list_name.append(person)
        # print("ID - " + str(row[0]) + ", Name - " + row[1] + ', Age -' + str(row[2]))
    cursor.close()
    connection.close()
    return list_name

read_database_people(people_list)
print(people_list)

def read_database_drinks(list_name):
    connection = pymysql.connect(
		"localhost",
		"root",
		"barnformtreefred",
		"ali_test"
	)
    cursor = connection.cursor()
    cursor.execute("SELECT drink_id, drink_name, drink_container, volume FROM drinks")
    rows = cursor.fetchall()
    for row in rows:
        drink = Drink(row[1], row[2], row[3])
        list_name.append(drink)
    cursor.close()
    connection.close()
    return list_name
