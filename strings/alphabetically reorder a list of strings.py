namelist = []

while True:

    userinput = input("> ")

    if userinput == "done":
        break

    namelist.append(userinput.capitalize())

namelist.sort()

print(namelist)




    
