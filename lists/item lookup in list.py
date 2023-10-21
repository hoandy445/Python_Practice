userlist = []
print("Enter words or numbers. Press enter to add another item. Type 'done' when finished.")

while True:
    userinput = input("> ")
    if userinput == "done":
          break
    userlist.append(userinput)
    
print("Your list: ", userlist)

print("You are now able to lookup items within your list. Input a number to search, or type 'done' to terminate the program.")

while True:
    userinput = input("> ")
    
    if userinput == "done":
        print("Closing program...")
        break
   
    try:
         userinput = int(userinput)
         
         if userinput > len(userlist) or userinput <= 0:
              print("The number", userinput, "does not correspond to an item within the list.")
              continue
    
    except:
        print("Invalid input. Type a number to lookup an item within your list, or type 'done' to terminate the program.")
        continue
    
    index = userlist[userinput - 1] 
    print(userinput, "is the item", "'" + index + "'", "in your list")
