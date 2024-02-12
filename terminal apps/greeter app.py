# FILE SETUP
namelist = r'C:\Users\hoand\Desktop\Programming\Python Practice\terminal apps\greeter name list.txt'
file = open(namelist)
readfile = file.read()
addname = open(namelist,mode="a")
names = readfile.split()


# MODULES

import os
from time import sleep
import re


# FUNCTIONS

def display_title():
    print("\t***************************************************")
    print("\t***   Welcome to Greeter, old and new friends!  ***")
    print("\t*******   Currently remembering %d names.   *******" %(len(names)))
    print("\t****************************************************")

def display_names(names):
    names.sort()
    counter = 0
    for name in names:
        if counter%10 == 0:
            sleep(1.5)
            os.system('cls') 
            display_title()
        sleep(0.06)
        print(name)
        counter += 1

def check_name(userinput):
    userinput = input("Enter your name:\n> ")
    checkname = re.fullmatch("[a-zA-Z]+",userinput)

    if checkname is not None and userinput not in names:
        print("We have not met before, %s. Welcome!" %userinput.title())
        addname.write("\n"+userinput)
    elif checkname is not None and userinput in names:
        print("Welcome back, %s!" %userinput.title())
    else:
        print("The name you entered, %s, does not seem like a real name." %userinput.title())


# MAIN PROGRAM

while True:
    sleep(1.5)
    os.system('cls')
    display_title()
    
    print('''
          Enter "1" to display all registered names.
          Enter "2" to register a new name.
          Enter "q" to close application.\n''')
    
    userinput = input("Please enter a selection:\n> ")
    
    if userinput == "1":
        display_names(names)
    elif userinput == "2":
        check_name(userinput)
        break
    elif userinput == "q":
        print("Closing program...")
        break
    else:
        print("Selection not found. Please try again.")
        continue


