import pymysql

from classes.classes import Drink
from classes.person import Person
def write_drinks_db(list_name):
    drinks2 = []
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
        drinks2.append(drink)
    
    for drink in list_name:
        drink_found = False
        for drink_1 in drinks2:
            if drink.drink_name == drink_1.drink_name:
                drink_found = True
        if drink_found == False:
            connection = pymysql.connect(
                "localhost",
                "root",
                "barnformtreefred",
                "ali_test"
                )
            cursor = connection.cursor()
            cursor.execute(f"INSERT INTO drinks (drink_name, container, volume) values ('{drink.drink_name}', '{drink.container}', '{drink.volume}')")
            connection.commit()

def write_people_db(list_name):
    people_1 = []
    connection = pymysql.connect(
        "localhost",
        "root",
        "barnformtreefred",
        "ali_test"
        )
    cursor = connection.cursor()
    cursor.execute("SELECT person_name, age FROM person")
    rows = cursor.fetchall()
    for row in rows:
        person = Person(row[0], row[1])
        people_1.append(person)
    
    for person in list_name:
        # print(people_list)
        person_found = False
        for person_1 in people_1:
            if person.name == person_1.name:
                person_found = True
        if person_found == False:
            connection = pymysql.connect(
                "localhost",
                "root",
                "barnformtreefred",
                "ali_test"
                )
            cursor = connection.cursor()
            cursor.execute(f"INSERT INTO person(person_name, age) values ('{person.name}', '{person.age}')")
            connection.commit()
           
