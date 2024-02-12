items = {}

items = {"20/up Santolla King Crab Legs" : "Item#: 17620656",
        "Haring 4# Miscut Catfish Fillets" : "Item#: 33520501",
        "7/9 Catfish Fillet Superior" : "Item#: 33520510"  }

# print(items)

# for key in items:
#     print(key)

for value in items:
    print(items[value])

# print(items.get("20/up Santolla King Crab Legs")) #get value by inputting key
# if items.get("chicken breast"): #if the item is not in the dictionary, returns None
#     print("Item is in dictionary.")
# else:
#     print("Item is not in dictionary.")


# keys = items.keys() #makes a list of the keys within the dictionary
# print(keys)

# values = items.values() #makes a list of the values
# print(values)

# kv = items.items() #makes a list of the kv pairs as tuples
# print(kv)

# for k,v in items.items(): #if iterating over dict.items(), two iteration variables are required, and iterates over both key and value
#     print(k, v)

# items.update({"40# Chicken Thigh Bulk": "Item#: P0300086"}) #update dictionary with new key-value pair
# items.update({"20/up Santolla King Crab Legs" : "Item#: 0998871"}) #can also update existing key-value pair with new key-value pair
# print(items)

# items.pop("20/up Santolla King Crab Legs") #removes key-value pair in dictionary by inputting key into argument
# print(items)

# items.popitem() #removes last entry in dictionary
# print(items)

# items.clear() #clears everything in dictionary
# print(items)