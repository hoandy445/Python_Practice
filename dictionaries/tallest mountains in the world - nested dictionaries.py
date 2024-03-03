# to be completed:


# completed:
# Create a new dictionary, where the keys of the dictionary are once again the mountains' names. This time, the values of the dictionary are another dictionary. This dictionary should contain the elevation in either meters or feet, and the range that contains the mountain. For example: {'everest': {'elevation': 8848, 'range': 'himalaya'}}.
# Print out just the mountains' names.
# Print out just the mountains' elevations.
# Print out just the range for each mountain.
# Print out a series of statements that say everything you know about each mountain: "Everest is an 8848-meter tall mountain in the Himalaya range."

mountains = {
        'everest':      {'height':8848,'range':'himalayas'},
        'k2':           {'height':8611,'range':'karakoram'},
        'kangchenjunga':{'height':8586,'range':'himalayas'},
        'lhotse':       {'height':8516,'range':'himalayas'},
        'makalu':       {'height':8486,'range':'himalayas'}
} # format = mountain:meters


# for mountain in mountains:
#     print("Mountain: ",mountain)

# for mountain,mountain_info in mountains.items():
#     print(mountain_info['height'])

# everest = mountains['everest']
# everest = everest['height']
# print(everest)

# for mountain,mountain_info in mountains.items():
#     print(mountain_info['range'])

for mountain,mountain_info in mountains.items():
    height = mountain_info['height']
    rng = mountain_info['range']
    print(f"{mountain.title()} is a {height}-meter tall mountain in the {rng.title()} range.")