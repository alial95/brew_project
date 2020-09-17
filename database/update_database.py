import pymysql

from classes.drink import Drink
from classes.person import Person
from classes.preference import Preference


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
def write_drinks_db(list_name, credentials=CREDENTIALS):
    drinks2 = []
    connection = pymysql.connect(**credentials)
    cursor = connection.cursor()
    cursor.execute("SELECT drink_id, drink_name, container, volume FROM drinks")
    rows = cursor.fetchall()
    for row in rows:
        drink = Drink(row[1], row[2], row[3])
        drinks2.append(drink)
    
    for drink in list_name:
        drink_found = False
        for drink_1 in drinks2:
            if drink.drink_name == drink_1.drink_name:
                drink_found = True
        if drink_found == False:
            connection = pymysql.connect(**credentials)
            cursor = connection.cursor()
            cursor.execute(f"INSERT INTO drinks (drink_name, container, volume) values ('{drink.drink_name}', '{drink.container}', '{drink.volume}')")
            connection.commit()

def write_people_db(list_name, list_2, credentials=CREDENTIALS):
    people_1 = []
    people_2 = []
    for obj in list_2:
        people_2.append(obj.drink_id)
    counter = 0
    connection = pymysql.connect(**credentials)
    cursor = connection.cursor()
    cursor.execute("SELECT person_name, age, favourite_drink_id FROM person")
    rows = cursor.fetchall()
    for row in rows:
        person = Person(row[0], row[1])
        people_1.append(person)
    for person in list_name:
        counter += 1
        person_found = False
        for person_1 in people_1:
            if person.name == person_1.name:
                person_found = True
        if person_found == False:
            connection = pymysql.connect(**credentials)
            cursor = connection.cursor()
            cursor.execute(f"INSERT INTO person(person_name, age, favourite_drink_id) values ('{person.name}', '{person.age}', '{people_2[counter-1]}')")
            connection.commit()
