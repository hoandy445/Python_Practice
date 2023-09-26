# shortens names into 3 letters - the first, middle, and last letters

userinput = input("> ")

length = len(userinput)

shorten = (userinput[0] + userinput[length//2] + userinput[length - 1])

print(shorten)


    
