import os, csv, pymysql
from classes.preference_test import Preference, select_preference
from classes.round import take_order, Round
from classes.person import Person, make_person
from classes.drink import Drink, make_drink
from menu.menu import show_menu_and_get_selection
from persistence.file_handling import write_to_file_people, write_to_file_drink, write_preference_to_file, read_from_file, read_from_file_1
from utils.utils import clear_screen
from database.read_from_database import read_database_people, read_database_drinks, read_preference
from database.update_database import write_drinks_db, write_people_db 
list_drinks, people_list, favourite_drink_list, round_drinks = [], [], [], []


def run_app():
    read_database_drinks(list_drinks)    
    read_database_people(people_list)
    read_preference(favourite_drink_list)
    while True:
        selection = show_menu_and_get_selection()
        if selection == 1:
            make_drink(list_drinks)
        elif selection == 2:
            make_person(people_list)
        elif selection == 3:
            for person in people_list:
                print(person)
            input("Please press enter to return to menu: ")
        elif selection == 4:
            for drink in list_drinks:
                print(drink)
            input("Please press enter to return to menu.")
        elif selection == 5:
            take_order(people_list, round_drinks, list_drinks)
        elif selection == ValueError:
            show_menu_and_get_selection
        elif selection == 6:
            # read_from_file_2('example.csv', 'example_2.csv', preference_list)
            # print(preference_list)
            select_preference(people_list, favourite_drink_list, list_drinks)
            input("Please press enter to return to menu.")
        elif selection == 7:
            for favourite in favourite_drink_list:
                print(favourite)
            input("Please press enter to return to menu.")
        elif selection == 8:
            write_drinks_db(list_drinks)
            write_people_db(people_list, favourite_drink_list)
            print("Bye!")
            exit()



run_app()