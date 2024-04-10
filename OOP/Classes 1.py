class Rocket():

    def __init__(self):
        self.x = 0
        self.y = 0

    def move_up(self):
        self.y += 1

def check_altitude(object_position):
    print('Rocket altitude:', object_position) #use dot notation to access object variables/methods

# my_rocket = Rocket() #creates an object - a single instance of the class
# check_altitude()

# my_rocket.move_up()
# check_altitude()

my_rockets = [Rocket() for x in range(0,5)] # list comprehension to create five rockets
# these are all their own separate instance, which can be seen when printed because each rocket is stored in a 
# different memory location
print(my_rockets) 

check_altitude(my_rockets[0].y)
my_rockets[0].move_up()

check_altitude(my_rockets[0].y)
check_altitude(my_rockets[1].y)
