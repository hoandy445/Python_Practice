accounts = {}

while True:
    print("Type 'create' to create an account, or 'login' to log into an existing account.")
    
    userinput = input("> ")
    
    if userinput == "create":
        usern = input("Enter a username: ")
        passw = input("Enter a password: ")
        for key in accounts:
            if usern == key: print("Username is already taken, please try again."); continue
        accounts.update({usern:passw})
        continue
    
    if userinput == "login":
        if len(accounts) < 1: print("No accounts found in database."); continue
        while True:
            usern = input("Enter username: ")
            passw = input("Enter password: ")
            tup = (usern,passw)
            for k,v in accounts.items():
                if (k,v) == tup:
                    print("Login successful!"); quit()
            print("Could not access acount. Please try again.")
            continue
