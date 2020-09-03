import csv, os
from classes.drink import Drink
from classes.person import Person
from classes.round import Round
from classes.preference import Preference
def write_to_file_people(file_name, list_name):
    with open(file_name, 'w', newline='') as csvfile:
        add_list= csv.writer(csvfile, delimiter=' ', lineterminator='\n')
        for person in list_name:
            add_list.writerow([person.name, person.age])


def write_to_file_drink(file_name, list_name):
    with open(file_name, 'w', newline='') as csvfile:
        add_list= csv.writer(csvfile, delimiter=' ', lineterminator='\n')
        for drink in list_name:
            add_list.writerow([drink.drink_name, drink.container, drink.volume])
      
def write_preference_to_file(filename, list_name):
    with open(filename, "r+", newline='') as file:
        new_file = csv.DictWriter(file, ['Name:', 'Drink:'], delimiter=' ')
        new_file.writeheader()
        for row in list_name:
            new_file.writerow({'Name:': row.name, 'Drink:': row.drink_name})




def read_from_file(file_name, list_name):
    with open(file_name, 'r+') as csvfile:
       new_thing = csv.reader(csvfile, delimiter= ' ')
       for row in new_thing:
           drink = Drink(row[0], row[1], row[2])
           list_name.append(drink)


def read_from_file_1(file_name, list_name):
    with open(file_name, 'r+') as csvfile:
       new_thing = csv.reader(csvfile, delimiter= ' ')
       for row in new_thing:
           person = Person(row[0], row[1])
           list_name.append(person)