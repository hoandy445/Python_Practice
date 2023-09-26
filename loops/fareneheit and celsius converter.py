while True:

    userinput = input("Convert to Celsius or Farenheit?\n> ")

    if userinput == "celsius" or userinput == "Celsius":
        
        while True:
            f = input("Enter Farenheit temperature: ")
            
            try:
                f = float(f)

            except:
                print("Invalid input. Please type a number.")
                continue

            c = (f - 32) * (5/9)
            print(f, "F is equal to", c, "C")
            break

    
    elif userinput == "farenheit" or userinput == "Farenheit":
        
        while True:
            c = input("Enter Celsius temperature: ")
            
            try:
                c = float(c)
            
            except:
                print("Invalid input. Please type a number.")
                continue
            
            f = c * (9/5) + 32
            print(c, "C is equal to", f, "F")
            break


    else:
        print("Invalid input. Enter 'Celsius' to convert Farenheit to Celsius, or 'Farenheit' to convert Celsius to Farenheit.")
        continue

    
    restart = input("Make another conversion? Enter Y to restart.\n> ")
    
    if restart == "Y" or restart == "y":
        continue
    else:
        print("Program terminated.")
        break
