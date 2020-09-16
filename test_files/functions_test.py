import unittest
from classes.person import Person, make_person

class MakePerson(unittest.TestCase):
    '''Tests the make person function.'''
    
    def test_store_person(self):
        """Test that a single response is stored properly."""
        tests = []
        make_person(tests)
        for person in tests:
            self.assertEqual(person.name, new_person.name)



new_person = Person('bob', 32)

if __name__ == '__main__':
    unittest.main()