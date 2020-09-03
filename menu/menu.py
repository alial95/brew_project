from utils.utils import clear_screen

def show_menu_and_get_selection():
    clear_screen()
    menu_text = """
Welcome to BrIW v0.1!
Please, select an option below by entering a number:
    [1] Make drink from user input
    [2] Make new person from user input
    [3] Print list of people
    [4] Print list of drinks
    [5] Save list to file
    [6] Make round 
    [7] Select preference
    [8] Print preference list
    [9] Save preference list to file
    [10] Exit
    """
    print(menu_text)
    while True:
        try:
            return int(input("Enter a number: "))
        except ValueError:
            print("Please enter a valid number.")