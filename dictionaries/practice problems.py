#make dictionary key:value pair using items in lists
# keys = ['Ten', 'Twenty', 'Thirty']
# values = [10, 20, 30]

# d = {}
# counter = 0
# for key in keys:
#     d[key] = d.get(key,values[counter])
#     counter = counter + 1


# d = dict(zip(keys,values))
# print(d)

# d = {}
# for i in range(len(keys)):
#     d[keys[i]] = values[i]
# print(d)

# d = {}
# for i in range(len(keys)):
#     d.update({keys[i]:values[i]})
# print(d)

#merge two dictionaries into one
# dict1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
# dict2 = {'Thirty': 30, 'Fourty': 40, 'Fifty': 50}

# dict1.update(dict2)
# print(dict1)

#find value in nested keys
sampleDict = {
    "class": {
        "student": {
            "name": "Mike",
            "marks": {
                "physics": 70,
                "history": 80
            }
        }
    }
}
print(sampleDict["class"]["student"]["marks"]["history"])