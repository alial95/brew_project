from database.read_from_database import show_preferences

class Round():
    def __init__(self, name, drink_name):
        self.name = name
        self.drink_name = drink_name
        self.order = dict(zip(self.name, self.drink_name)) 

    def __repr__(self):
        return f'{self.name} is having a {self.drink_name}.'
    
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
def take_order(list_1, list_2, list_3, dict_1):
    people = []
    drinks = []
    len_drinks = len(list_3)
    for person in list_1:
        person_found = False
        for name in list_2:
            if person.name == name.name:
                person_found = True       
        if person_found == False:
            people.append(person.name)
            show_preferences()
            print(f"What does {person.name} want to drink?")
            counter = 1
            for drink in list_3:
                print(f"{counter}: {drink.drink_name}")
                counter +=1
            order = order_num(len_drinks)
            order -= 1
            drinks.append(list_3[order].drink_name)
    whole_order = Round(people, drinks)
    dict_1 = whole_order.order
    for person, drink in dict_1.items():
        print("Name: " + person + " Drink: " + drink)
    return dict_1