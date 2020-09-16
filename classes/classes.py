class Drink:
    def __init__(self, drink_name, container, volume):
        self.drink_name = drink_name
        self.container = container
        self.volume = int(volume)

    def have_drink(self, volume_poured):
        self.volume -= volume_poured

    def __repr__(self):
        return (f"{self.drink_name}, {self.container}, {self.volume}")

class Person:
    def __init__(self, name, age):
        """Get the human's name and age."""
        self.name = name
        self.age = age
    def __repr__(self):
        return f'{self.name}, {self.age}'

class Preference():
    def __init__(self, name, drink_name):
        self.name = name
        self.drink_name = drink_name

    def __repr__(self):
        return f"{self.name}'s favourite drink is {self.drink_name}."

class Round():
    def __init__(self, name, drink_name):
        self.name = name
        self.drink_name = drink_name
    def __repr__(self):
        return f'{self.name} is having a {self.drink_name}.'