import pymysql
from classes.preference import Preference
from classes.drink import Drink
from classes.person import Person


CREDENTIALS = {
    "host": "localhost",
    "port": 3306,
    "user": "root",
    "password": "barnformtreefred",
    "db": "ali_test"
}
CREDENTIALS_DOCKER = {
    'host':'localhost',
    'port': 3306,
    'user':'root',
    'password': 'root_password',
    'db': 'brew'
}

def read_database_people(list_name, credentials=CREDENTIALS):
    connection = pymysql.connect(**credentials)
    cursor = connection.cursor()
    cursor.execute("SELECT person_name, age, favourite_drink_id FROM person")
    rows = cursor.fetchall()
    for row in rows:
        person = Person(row[0], row[1])
        list_name.append(person)
    cursor.close()
    connection.close()
    return list_name
def read_preference(list_name, credentials=CREDENTIALS):
    connection = pymysql.connect(**credentials)
    cursor = connection.cursor()
    cursor.execute("SELECT person_id, person_name, d.drink_name, favourite_drink_id FROM person join drinks as d on favourite_drink_id = d.drink_id order by person_id")
    rows = cursor.fetchall()
    for row in rows:
        preference = Preference(row[1], row[2], row[3])
        list_name.append(preference)
    cursor.close()
    connection.close()
    return list_name
def read_database_drinks(list_name, credentials=CREDENTIALS):
    connection = pymysql.connect(**credentials)
    cursor = connection.cursor()
    cursor.execute("SELECT drink_id, drink_name, container, volume FROM drinks")
    rows = cursor.fetchall()
    for row in rows:
        drink = Drink(row[1], row[2], row[3])
        list_name.append(drink)
    cursor.close()
    connection.close()
    return list_name

def show_preferences(credentials=CREDENTIALS):
    connection = pymysql.connect(**credentials)
    cursor = connection.cursor()
    cursor.execute("SELECT person_name, d.drink_name, favourite_drink_id FROM person join drinks as d on favourite_drink_id = d.drink_id")
    rows = cursor.fetchall()
    print("List of Preferences: ")
    for row in rows:
        print(row[0]  + ":  " + row[1])  
    cursor.close
    connection.close