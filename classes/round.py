
class Round():
    def __init__(self, name, drink_name):
        self.name = name
        self.drink_name = drink_name
    def __repr__(self):
        return f'{self.name} is having a {self.drink_name}.'

def take_order(list_1, list_2, list_3):
    flag = True
    while flag == True:
        for person in list_1:
            print(f"{person.name}")
        person_1 = input("Who is getting a drink? ")
        if person_1 in list_2:
            print("Please select someone else: ")
        for name in list_3:
            print(name)
        drink = input("What drink would you like? ")
        order = Round(person_1, drink)      
        list_2.append(order)
        for name in list_2:
            print(name)
        new_person = input("Would you like to add another person? Press n to stop: ")
        if new_person == 'n':
            flag = False
    print(list_2)
    print(input("Please press enter to return to the main menu."))
    return person, drink