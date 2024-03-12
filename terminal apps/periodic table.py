import json

# display the main menu options
def display_main_menu():
    print('''
*** MAIN MENU ***
Enter '1' to display all saved elements.
Enter '2' to add a new element.
Enter '3' to add information about an element.
Enter 'q' to close application.
''')

# display submenu options for adding information about an element
def display_add_info_submenu(symbol):
    print(f'''
*** ADD INFORMATION MENU ***
Selected symbol: {symbol}
{symbol} : {periodic_table[symbol]}
Enter '1' to add the element name.
Enter '2' to add the atomic number.
Enter '3' to add the row number.
Enter '4' to add the column number.
Enter '5' to add information to a different element.
Enter 'm' to return to the main menu.
''')

# display all elements in the periodic table
def display_all_elements():
    for key,value in sorted(periodic_table.items()):
        print(key,value)

# prompt user to return to the main menu
def return_to_menu():
    input("Press 'Enter' to return to the main menu.")

# prompt user to return to the submenu
def return_to_submenu():
    input("Press 'Enter' to continue...")

# add a new element to the periodic table
def add_new_element():
    symbol = input("Enter the symbol of the chemical (up to three letters):\n> ").title().strip()
    if string_validation_check(symbol) is True:
        if periodic_table.get(symbol) is None:
            periodic_table[symbol] = {}
            print(f"{symbol} has been added successfully.")
        else:
            print(f"{symbol} has already been added. Operation cancelled.")

# add the name of an element
def add_element_name(symbol):
    element_name = input("Enter the name of the element (e.g. potassium, sodium, etc.):\n> ").title().strip()
    if string_validation_check(element_name) is True:
        periodic_table[symbol].update({'Name':element_name})
        print(f"Element name '{element_name}' has been successfully added to the element '{symbol}'.")

# add the atomic number of an element
def add_atomic_number(symbol):
        atomic_number = input("Enter the atomic number of the element:\n> ").strip()
        if integer_validation_check(atomic_number) is True:
            if integer_range_validation_check(atomic_number,1,118) is True:
                periodic_table[symbol].update({'Atomic Number':atomic_number})
                print(f"Atomic number '{atomic_number}' has successfully been added to the element '{symbol}'.")

# add the row number of an element
def add_row_number(symbol):
    row_number = input("Enter the row number of the element:\n> ").strip()
    if integer_validation_check(row_number) is True:
        if integer_range_validation_check(row_number,1,7) is True:
            periodic_table[symbol].update({'Row Number':row_number})
            print(f"Row number '{row_number}' has successfully been added to the element '{symbol}'.")

# add the column number of an element
def add_column_number(symbol):
    column_number = input("Enter the column number of the element:\n> ").strip()
    if integer_validation_check(column_number) is True:
        if integer_range_validation_check(column_number,1,18) is True:
            periodic_table[symbol].update({'Column Number':column_number})
            print(f"Column number '{column_number}' has successfully been added to the element '{symbol}'.")

# allow the user to change the selected symbol
def change_symbol_selection():
    new_symbol = input("Enter the symbol name of the element you would like to select (up to three letters):\n> ").title().strip()
    if new_symbol in periodic_table:
        print(f"Succesfully selected symbol '{new_symbol}'.")
        return(new_symbol)
    else:
        input("That symbol has not yet been added to the periodic table. Operation cancelled.")

# read the periodic table data from a JSON file
def read_file():
    try:
        with open("periodic_table.json","r") as file_handle:
            periodic_table = json.load(file_handle)
            return periodic_table
    except FileNotFoundError:
        print("Starting blank periodic table...")
        periodic_table = {}
        return periodic_table

# write the periodic table data to a JSON file
def write_to_file():
    try:
        with open("periodic_table.json", "w") as file_handle:
            json.dump(periodic_table, file_handle)
    except FileNotFoundError:
        print("Periodic table could not be written to .json file.")
        quit()

# validate whether user input is an integer
def integer_validation_check(user_input):
    if user_input.isnumeric() is False:
        print("Input must be a number. Operation cancelled.")
        return False
    else:
        return True
    
# validate whether user input is a string
def string_validation_check(user_input):
    if user_input.isalpha() is False:
        print("Input must only contain letters. Operation cancelled.")
        return False
    else:
        return True

# validate whether user input is within a specified range
def integer_range_validation_check(user_input, min_number, max_number):
    if int(user_input) >= min_number and int(user_input) <= max_number:
        return True
    else:
        print(f"Input must be greater than or equal to {min_number} and less than or equal to {max_number}. Operation cancelled. ")
        return False

def get_atomic_number(element):
    return element[1]['Atomic Number']


# Main program
periodic_table = read_file()

while True:
    display_main_menu()
    user_input = input("Please enter a selection:\n> ")

    if user_input == '1': 
        display_all_elements()
        return_to_menu()

    elif user_input == '2':
        add_new_element()
        return_to_menu()
    
    # Add information about elements
    elif user_input == '3':
        
            symbol = input("Enter the symbol name of the element you would like to add information to:\n> ").title().strip()
            if symbol in periodic_table:
                while True:
                    display_add_info_submenu(symbol)
                    user_input = input("Please enter a selection:\n> ")

                    if user_input =='1':
                        add_element_name(symbol)
                        return_to_submenu()
                    elif user_input == '2':
                        add_atomic_number(symbol)
                        return_to_submenu()
                    elif user_input == '3':
                        add_row_number(symbol)
                        return_to_submenu()
                    elif user_input == '4':
                        add_column_number(symbol)
                        return_to_submenu()
                    elif user_input == '5':
                        symbol = change_symbol_selection()
                        return_to_submenu()
                    elif user_input =='m':
                        break
                    else:
                        print(f"'{user_input}' is not a valid selection.")
            else:
                print(f"{symbol} has not yet been added to the periodic table.")
                return_to_menu()

    elif user_input == 'q':
        print("Closing application...")
        break
    
    else:
        print(f"'{user_input}' is not a valid selection")
        return_to_menu()

write_to_file()
