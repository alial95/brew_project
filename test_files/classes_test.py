import unittest
from classes.classes import Round, Person, Preference, Drink
class PersonTest(unittest.TestCase):
    '''Test the Person Class.'''
    def test_person_1(self):
        self.assertEqual(test_person.name, expected_person_name)
    def test_person_age(self):
        self.assertEqual(test_person.age, expected_person_age)

class DrinksTest(unittest.TestCase):
    '''Test the Drink Class.'''
    def test_drink_name(self):
        self.assertEqual(test_drink.drink_name, expected_drink_name)    
    def test_drink_container(self):
        self.assertEqual(test_drink.container, expected_drink_container)
    def test_drink_volume(self):
        self.assertEqual(test_drink.volume, expected_drink_volume)

class PreferenceTest(unittest.TestCase):
    '''Test the Preference Class.'''
    def test_preference_name(self):
        self.assertEqual(test_preference.name, expected_preference_name)
    def test_preference_drink(self):
        self.assertEqual(test_preference.drink_name, expected_preference_drink)

class RoundTest(unittest.TestCase):
    '''Test the Round Class.'''
    def test_round_name(self):
        self.assertEqual(test_round.name, expected_round_name)
    def test_round_drink(self):
        self.assertEqual(test_round.drink_name, expected_round_drink)

test_preference = Preference('steve', 'cola')
expected_preference_name = 'steve'
expected_preference_drink = 'cola'
test_person = Person('bob', 53)
expected_person_name = 'bob'
expected_person_age = 53
test_drink = Drink('cola', 'bottle', 500)
expected_drink_name = 'cola'
expected_drink_container = 'bottle'
expected_drink_volume = 500
test_round = Round('chris', 'lemonade')
expected_round_name = 'chris'
expected_round_drink = 'lemonade'


if __name__ == '__main__':
    unittest.main()

