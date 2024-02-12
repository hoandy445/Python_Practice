### MODULES ###
import os
import pickle
from time import sleep


### FILE PICKLING SETUP ###

try: 
    fhandr = open('namelist.pydata', 'rb')
    namelist = pickle.load(fhandr)
    namelist.sort()
    fhandr.close()
except: 
    namelist = []


### FUNCTIONS ###
def display_title():
    print("**********************************************************************")
    print("*** Welcome to Greeter! Hello to both old friends and new friends! ***")
    print("**********************************************************************")

def display_names(names):
    counter = 0 # used to manipulate the amount of names that will appear for each block when the user requests to display names

    for name in names:
        if counter%10 == 0:
            sleep(0.5)
            os.system('cls')
            display_title()

        print(name)
        sleep(0.05)
        counter += 1

def add_new_name():
        try:
            fhandw = open('namelist.pydata', 'wb')
            pickle.dump(namelist,fhandw)
            fhandw.close()
        except:
            print("I wasn't able to remember that game. Sorry!")   

### MAIN PROGRAM ###

userinput = ""

while userinput != "q":
    sleep(1)
    os.system('cls')
    display_title()
    
    print("Enter '1' to show all old friends.")
    print("Enter '2' to introduce a new friend.")
    print("Enter 'q' to quit.")
    userinput = input("Please enter a selection: ")

    if userinput == "q": 
        print("Closing program. Have a nice day!")
        break
    
    elif userinput == "1":
        if len(namelist) > 0:
            display_names(namelist)
        else:
            print("I don't have any friends yet. :c")
    
    elif userinput == "2":
        userinput = input("I can't wait to meet! What is the new friend's name?\n> ")
        if userinput.lower() in namelist:
            print("Oh, I already know %s!" %userinput.title())
            continue
        else:
            namelist.append(userinput.lower())
            add_new_name()
    
    else:
        print("Oops, I didn't understand that selection.")
        continue


    

