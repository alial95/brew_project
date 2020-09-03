

class Preference():
    def __init__(self, name, drink_name):
        self.name = name
        self.drink_name = drink_name

    def __repr__(self):
        return f"{self.name}'s favourite drink is {self.drink_name}."

def select_preference(list_1, list_2, list_3):  
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
            order = int(input())
            order -= 1
            favourite_drink = Preference(person.name, list_3[order].drink_name) 
            print(favourite_drink)  
            list_2.append(favourite_drink)
