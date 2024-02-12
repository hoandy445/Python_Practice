import pickle #pickling an object (list, dictionary, etc) packages it up and stores it on disk in a way that we can get it back in its original form later

try:
    fhand = open('animals.pydata','rb')
    animals = pickle.load(fhand)
    fhand.close()
except:
    animals = []


if len(animals)>0:
    print("Registered animals: ")
    for animal in animals:
        print(animal)
else:
    print("I don't know any animals yet.")

new_animal = ""
while new_animal != "quit":
    print("\nPlease tell me a new animal to remember.")
    new_animal = input("Enter 'quit' to quit: ")
    if new_animal != "quit":
        animals.append(new_animal)


try:
    fhand = open('animals.pydata','wb')
    pickle.dump(animals, fhand) #dumps the list animals into fhand. it is not dumped in a format we can read
    fhand.close()

    print("\nI will remember the following animals: ")
    for animal in animals:
        print(animal)

except Exception as e:
    print(e)
    print("\nI couldn't figure out how to store the animals. Sorry.")