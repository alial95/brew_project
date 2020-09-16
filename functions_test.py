import unittest
from unittest.mock import MagicMock
from unittest.mock import patch
@patch('classes.person.make_person')
class MakePerson(unittest.TestCase):

    def test_make_new_person(self, mock_make_new_person):
        test_list = []
        mock_make_new_person.return_value = 'bob'
        actual_person = mock_make_new_person(test_list)
        expected_person = 'bob'
        self.assertEqual(actual_person, expected_person)
        print(*test_list)



"""""



# class MakePerson(unittest.TestCase):
#     '''Tests the make person function.'''
    
#     def test_store_person(self):
#         """Test that a single response is stored properly."""
#         tests = []
#         make_person(tests)
#         for person in tests:
#             self.assertEqual(person.name, new_person.name)



# new_person = Person('bob', 32)

if __name__ == '__main__':
    unittest.main()