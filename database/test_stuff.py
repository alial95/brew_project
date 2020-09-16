import pymysql
import csv
drinks = []
drinks2 = []
class Drink:
    def __init__(self, drink_name, container, volume):
        self.drink_name = drink_name
        self.container = container
        self.volume = int(volume)

    def have_drink(self, volume_poured):
        self.volume -= volume_poured

    def __repr__(self):
        return (f"{self.drink_name}, {self.container}, {self.volume}")

def read_from_file(file_name, list_name):
    with open(file_name, 'r+') as csvfile:
       new_thing = csv.reader(csvfile, delimiter= ' ')
       for row in new_thing:
           drink = Drink(row[0], row[1], row[2])
           list_name.append(drink)
           
read_from_file('persistence/example.csv', drinks)





def write_drinks_db(list_name):
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
    
    for drink in drinks:
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
            # cursor.execute("DELETE FROM drinks")
            for drink in list_name:
                cursor.execute(f"INSERT IGNORE INTO drinks (drink_name, container, volume) values ('{drink.drink_name}', '{drink.container}', '{drink.volume}')")
            connection.commit()
write_drinks_db(drinks)