def display_main_menu():
    print('''
Enter '1' to display all saved elements.
Enter '2' to add a new element.
Enter '3' to add information about an element.
Enter 'q' to close application.\n>       
''')

def display_add_info_submenu():
    print('''
Enter '1' to add the element name.
Enter '2' to add the atomic number.
Enter '3' to add the row number.
Enter '4' to add the column number.
Enter '5' to add information to a different element.
Enter 'm' to return to the main menu.
''')

def display_all_elements():
    for key,value in periodic_table.items():
        print(key,value)

def return_to_menu():
    input("Press 'Enter' to return to the main menu.")

def add_element():
    symbol = input("Enter the symbol of the chemical (up to three letters):\n> ").upper().strip()
    if periodic_table.get(symbol) is None:
        periodic_table[symbol] = {}
        print(f"{symbol} has been added successfully.")
    else:
        print(f"{symbol} has already been added. Operation cancelled.")


# main program

periodic_table = {}

while True:
    display_main_menu()
    user_input = input("Please enter a selection:\n> ")

    if user_input == '1': 
        display_all_elements()
        return_to_menu()

    elif user_input == '2':
        add_element()
    
    # add info about elements
    elif user_input == '3':
        while True:
            symbol = input("Enter the symbol name of the element you would like to add information to.")
            display_add_info_submenu()
            user_input = input("Please enter a selection:\n> ")

            #bookmark



    elif user_input == 'q':
        print("Closing application...")
        break
    
    else:
        print(f"'{user_input}' is not a valid selection")
        return_to_menu()
    