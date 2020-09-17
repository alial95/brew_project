

class Person:
    def __init__(self, name, age):
        """Get the human's name and age."""
        self.name = name
        self.age = str(age)
        self.list = list((self.name, self.age))
    def __repr__(self):
        return f'{self.name}, {self.age}'
    

def make_person(list_name):
    name_counter = 0
    while name_counter <= 0:
        name_input = input("Please enter the persons name: ")
        age_input = int(input("Please enter the persons age: "))
        person = Person(name_input, age_input)
        print(person)
        list_name.append(person)
        name_counter += 1
    return person

