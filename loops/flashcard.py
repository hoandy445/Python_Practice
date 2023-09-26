# flashcard program 1.1

accumulator = "a variable used in a loop to add up or accumulate a result"

decrement = "an update that decreases the value of a variable"

terms = [accumulator, decrement]
listofterms = "accumulator, decrement"

import random

random.shuffle(terms)

print("Type the word that matches the definition.")
print("List of terms:", listofterms)

grade = 0

for term in terms:

    print(term)
    userinput = input("> ")
    
    if term == accumulator:
        if userinput == "accumulator":
            grade = grade + 1

    if term == decrement:
        if userinput == "decrement":
            grade = grade + 1

print("Grade:", grade, "/ 2")
            


    