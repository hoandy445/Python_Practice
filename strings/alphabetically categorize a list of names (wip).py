namelist = []

while True:

    userinput = input("> ")

    if userinput == "done":
        break

    namelist.append(userinput)


def upper(names):
    names = names[0].upper() + names[1:]
    return names

smallest = None

for i in namelist:
    if smallest is None:
        smallest = i
    elif i < smallest:
        smallest = i
print(smallest, "smallest")

alphabetize = smallest

for k in namelist:
    if k > alphabetize:
        alphabetize = k
    print(alphabetize)



    
