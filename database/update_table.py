import pymysql
import csv
# from classes.drink import Drink
# from persistence.file_handling import read_from_file
drinks = []

class Drink:
    def __init__(self, drink_name, container, volume):
        self.drink_name = drink_name
        self.container = container
        self.volume = int(volume)

    def have_drink(self, volume_poured):
        self.volume -= volume_poured

    def __repr__(self):
        return (f"{self.drink_name}, {self.container}, {self.volume}")

# def read_from_file(file_name, list_name):
#     with open(file_name, 'r+') as csvfile:
#        new_thing = csv.reader(csvfile, delimiter= ' ')
#        for row in new_thing:
#            list_name.append(row)
#     return list_name

def read_from_file(file_name, list_name):
    with open(file_name, 'r+') as csvfile:
       new_thing = csv.reader(csvfile, delimiter= ' ')
       for row in new_thing:
           drink = Drink(row[0], row[1], row[2])
           list_name.append(drink)
           
read_from_file('persistence/example.csv', drinks)
print(drinks)


def write_drinks_db(list_name):
    connection = pymysql.connect(
        "localhost",
        "root",
        "barnformtreefred",
        "ali_test"
        )
    cursor = connection.cursor()
    cursor.execute("DELETE FROM drinks")
    for drink in list_name:
        cursor.execute(f"INSERT IGNORE INTO drinks (drink_name, drink_container, volume) values ('{drink.drink_name}', '{drink.container}', '{drink.volume}')")
    connection.commit()
write_drinks_db(drinks)
def write_people_db(list_name):
    connection = pymysql.connect(
        "localhost",
        "root",
        "barnformtreefred",
        "ali_test"
        )
    cursor = connection.cursor()
    cursor.execute("DELETE FROM person")
    for person in list_name:
        cursor.execute(f"INSERT IGNORE INTO person (first_name, age) values ('{person.name}', '{person.age}')")
    connection.commit()

# cursor.execute()
# drinks_list += [str(drink)]
#     print(drinks_list)
# print(drinks_list)
# for i in drinks_list:
#     sql = "INSERT INTO drinks (drink_name, drink_container, volume) values (%s, %s, %s)"