# to be completed:

# completed:
# Print out just the mountains' elevations in meters, by looping through the values of your dictionary and pulling out the first number from each list.
# Create a new dictionary, where the keys of the dictionary are still the mountains' names. This time however, the values of the dictionary should be a list of each mountain's elevation in meters, and then in feet: {'everest': [8848, 29029]}# The list of tallest mountains in the world provided all elevations in meters. Convert each of these elevations to feet, given that a meter is approximately 3.28 feet. You can do these calculations by hand at this point.
# Print out just the mountains' names, by looping through the keys of your dictionary.
# Print out just the mountains' elevations in feet, by looping through the values of your dictionary and pulling out the second number from each list.
# Print out a series of statements telling how tall each mountain is: "Everest is 8848 meters tall, or 29029 feet."

def meter_to_feet(meter):
    return meter*3.28

mountains = {'everest':8848,
        'k2' : 8611,
        'kangchenjunga':8586,
        'lhotse':8516,
        'makalu':8486} # format = mountain:meters

newdict = {} # format = mountain:[meters,feet]

for mountain,meters in mountains.items():
    feet = meter_to_feet(meters)
    newdict.update({mountain:[meters,feet]})


for mountain,height in newdict.items():
    meters = height[0]
    feet = height[1]
    print(f"Mountain: {mountain}\nHeight in meters: {meters}\nHeight in feet: {feet:.2f}")
