import pickle

try:
    fhandr = open('gamelist.pydata', 'rb')
    games = pickle.load(fhandr)
    print("Games currently being remembered: ")
    for i in games:
        print(i)

except:
    games = []


newgame = []
userinput = ""
while userinput != "q":
    userinput = input("Enter a game for me to remember. \nType 'q' to quit:  ")

    if userinput == "q":
        break
    elif userinput not in games:
        games.append(userinput.upper())
        newgame.append(userinput.upper())
    else:
        print("Oh, I already know that game!")
        continue


try:
    fhandw = open('gamelist.pydata','wb') # will try to open a file called "gamelist.pydata" in the same directory. if it does not exist, it creates an empty file
                                         # "wb" makes the file writeable, and writes into binary
                                         # the file handle is stored into the variable fhandw to be called upon later
    pickle.dump(games,fhandw) # uses pickle module "dump()" to dump contents of games into the file handle
    fhandw.close() # frees up system resources that were used during the file operation. remember to close!

    print("New games added: ")
    for game in newgame:
        print(game)

except Exception as e:
    print(e)
    print("Oops! I could not remember that game.")