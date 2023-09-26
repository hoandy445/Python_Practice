# shorten string into 3 characters - the first, middle, and last characters

userinput = input("> ")

length = len(userinput)

shorten = (userinput[0] + userinput[length//2] + userinput[length - 1])

print(shorten)


    
