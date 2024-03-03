import os
import json
import re
import random


def display_menu():
    print(
        """
*************************************************************
*** World Wall - the app that stores words and definitions ***
**************************************************************
Enter '1' to view all words and meanings entered so far.
Enter '2' to store a new word and meaning.
Enter '3' to modify words.
Enter '4' to categorize words.
Enter 'q' to close application.
"""
    )

def display_modification_submenu():
            print(
'''
Enter '1' to modify the spelling of a word. 
Enter '2' to change the meaning of a word. 
Enter '3' to delete a word.
Enter '4' to delete all words
Enter any other key to return to main menu.
''')

def display_words(dictionary):
    if len(dictionary) > 0:
        print("word : meaning\n_______________\n")
        for word, meaning in sorted(dictionary.items()):
            if not isinstance(meaning, dict):
                print(f"{word}: {meaning}")
            else:
                print(f"(CATEGORY) {word}: {meaning}")
    else:
        print("No words to display.")

def add_new_word(dictionary):  # extract user input and add to dictionary
    new_word = input("Please enter the new word:\n> ").lower().strip()

    if new_word not in dictionary:
        new_meaning = input("Please enter the meaning:\n> ").lower().strip()

        if word_validation(new_word) is True and meaning_validation(new_meaning) is True:
            print("Storing new word...")
            dictionary[new_word] = new_meaning

        else:
            print("New word could not be added. Words may only contain letters and spaces and cannot be blank. Meanings may only contain letters, spaces, commas, periods, and cannot be blank. Please try again.")

    else:
        print("That word already exists within Word Wall.")

def read_file():  # attempt to read json file or start new dictionary on failure
    try:
        with open("wordwall_dictionary.json", "r") as file_handle:
            wordwall_dictionary = json.load(file_handle)
            return wordwall_dictionary

    except FileNotFoundError:
        print("Could not open json file. Starting new dictionary.")
        wordwall_dictionary = {}
        return wordwall_dictionary

def write_to_file(dictionary):  # attempt to write dictionary to json file or shutdown on failure
    try:
        with open("wordwall_dictionary.json", "w") as file_handle:
            json.dump(dictionary, file_handle)

    except FileNotFoundError:
        print("Could not dump into json file. Closing application...")
        quit()

def modify_word(dictionary):
    old_word = input("Please enter which word you would like to modify.\n> ").lower().strip()
    if old_word in dictionary:
        new_word = input("Please enter how you would like this word to be spelled.\n> ").lower().strip()
        if word_validation(new_word) is True:
            meaning = dictionary[old_word]
            del dictionary[old_word]
            dictionary.update({new_word:meaning})
            print(f"'{old_word}' has been succesfully modified to '{new_word}'.")
        else:
            print("The new spelling of the word must only contain letters or spaces and cannot be blank. Please try again.")
    else:
        print("That word does not exist in Word Wall yet.")

def modify_meaning(dictionary):
    word = input("Please enter which word meaning you would like to modify.\n> ").lower().strip()
    if word in dictionary:
        new_meaning = input("Please enter the new meaning.\n> ").lower().strip()
        if meaning_validation(new_meaning) is True:
            dictionary[word] = new_meaning
            print(f"The meaning of '{word}' was sucessfully modified.")
        else:
            print("Your input must only contain letters, spaces, commas, periods, and cannot be blank. Please try again.")
    else:
        print("That word does not exist in Word Wall yet.")

def delete_word(dictionary):
    word = input("Please enter the word you would like to delete.\n> ").lower().strip()
    if word in dictionary:
        del dictionary[word]
        print(f"'{word}' was sucessfully deleted.")
    else:
        print("Unable to delete word. The spelling your input may be inaccurate, or the word may not yet exist in Word Wall.")

def delete_all_words(dictionary):
    user_choice = input("This action is not reversible. Enter '1' to delete all words. Enter any other key to return to the main menu.\n> ")
    if user_choice == '1':
        print("All entries successfully deleted.")
        dictionary = {}
        return dictionary
    else:
        print("Operation cancelled.")

def return_to_menu():
    input("\nPress 'Enter' to return to main menu.")

def clear_screen():
    os.system("cls")

def word_validation(user_input):
    pattern = "[a-zA-Z]+[a-zA-Z ]*" # one or more letters, followed by zero or more letters or spaces
    word_validation = False
    if re.fullmatch(pattern,user_input):
        word_validation = True
    return word_validation

def meaning_validation(user_input):
    pattern = "[a-zA-Z]+[a-zA-Z\., ]*" # one or more letters, followed by zero or more letters, commas, periods, or spaces
    meaning_validation = False
    if re.fullmatch(pattern,user_input):
        meaning_validation = True
    return meaning_validation

def new_category(dictionary):
    category = input("Enter the name of the category you would like to create:\n> ")
    if category not in dictionary:
        dictionary.update({category:{}})
    else:
        print("That category already exists.")

def add_to_category():
    word = input("Enter the word you would like to categorize:\n> ")
    if word in wordwall_dictionary:
        category = input(f"Enter the category you would like to add {word} to:\n> ")
        if category in wordwall_dictionary:
            meaning = wordwall_dictionary[word]
            wordwall_dictionary[category].update({word:meaning})
            del wordwall_dictionary[word]
        else:
            print("That category does not exist.")
    else:
        print("That word is not in Word Wall.")

wordwall_dictionary = read_file()


while True:
    clear_screen()
    display_menu()
    user_choice = input("Please enter a selection.\n> ")
    clear_screen()

    if user_choice == "1":
        display_words(wordwall_dictionary)
        return_to_menu()

    elif user_choice == "2":
        new_entry = add_new_word(wordwall_dictionary)
        return_to_menu()

    # modify dictionary
    elif user_choice == "3":
        display_modification_submenu()
        user_choice = input("Please enter a selection.\n> ")
        if user_choice == '1':
            modify_word(wordwall_dictionary)
        elif user_choice == '2':
            modify_meaning(wordwall_dictionary)
        elif user_choice =='3':
            delete_word(wordwall_dictionary)
        elif user_choice =='4':
            wordwall_dictionary = delete_all_words(wordwall_dictionary)
        return_to_menu()

    elif user_choice == "4":
        user_choice = input("Enter '1' to add a new category. Enter '2' to move a word to a category.\n> ")
        if user_choice == '1':
            new_category(wordwall_dictionary)
        elif user_choice == '2':
            add_to_category()
        return_to_menu()

    elif user_choice == "q":
        break

    else:
        print(f"Your input '{user_choice}' is not a valid selection. Please try again.")
        return_to_menu()

write_to_file(wordwall_dictionary)
print("Closing application...")