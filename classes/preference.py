

class Preference():
    def __init__(self, name, drink_name, drink_id):
        self.name = name
        self.drink_name = drink_name
        self.drink_id = str(drink_id)
        self.list = list((self.name, self.drink_name, self.drink_id))

    def __repr__(self):
        return f"{self.name}'s favourite drink is {self.drink_name}."

def select_preference(list_1, list_2, list_3):
    len_drinks = len(list_3)  
    for person in list_1:
        person_found = False
        for name in list_2:
            if person.name == name.name:
                person_found = True
        if person_found == False:
            print(f"What is {person.name}'s favourite drink?")
            counter = 1  
            for drink in list_3:
                print(f"{counter}: {drink.drink_name}")
                counter += 1 
            order = order_num(len_drinks)
            favourite_drink = Preference(person.name, list_3[order].drink_name, order) 
            print(favourite_drink)  
            list_2.append(favourite_drink)

def order_num(len_drinks_list):
    while True:
        try:
            order = int(input("Enter a number: "))
            if order > len_drinks_list:
                print("That number is too high! Please enter a valid number.")
                continue
            else:
                return order
        except:
            print("That's not a number! Please enter a valid number.")  
