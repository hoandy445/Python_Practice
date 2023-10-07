# %d to format an integer, %g to format float point, %s to format string

apples = input("Input apple quantity: ")
apples = int(apples)

print("You have %d apples.(int)" %apples) # whatever %d is needs to be an integer, or you get a traceback
print("You have %g apples.(float)"%apples) # %g requires float, but an int is still a valid input
print("You have %s apples.(str)"%apples) # same with strings



dollars, cents = (25, 17)

print("You have %d dollars and %d cents."%(dollars,cents))


name = "Andy"

print("Hello, my name is %s."%name)



