
class Drink:
    def __init__(self, drink_name, container, volume):
        self.drink_name = drink_name
        self.container = container
        self.volume = int(volume)

    def have_drink(self, volume_poured):
        self.volume -= volume_poured

    def __repr__(self):
        return (f"{self.drink_name}, {self.container}, {self.volume}")


def make_drink(list_name):
    name_counter = 0
    while name_counter <= 1:
        type_drink = input("\nPlease enter the drinks name: ")
        drink_container = input("Please enter the drinks container: ")
        volume = int(input("Please enter the drinks volume: "))
        drink = Drink(type_drink, drink_container, volume)
        list_name.append(drink)
        name_counter += 1


