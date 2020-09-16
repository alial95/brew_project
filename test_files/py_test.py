import unittest
from unittest.mock import MagicMock
# from classes.classes import Round
""" Testing the Menu for App.py """
def menu_test():
    mock_menu = MagicMock()
    mock_menu[3] = 'print list'
    mock_menu.__setitem__.assert_called_with(3, 'print list')
    mock_menu.__getitem__.return_value = 'result'
    

def append_object_list():
    list_mocks = []
    mock_2 = MagicMock
    list_mocks.append(mock_2)
    print(list_mocks)

mock_1 = MagicMock()
attrs = {'method.return_value': 3, 'other.side_effect': KeyError}
mock_1.configure_mock(**attrs)
test = mock_1.method()
mock_1.other()
print(test)
menu_test()
append_object_list()

