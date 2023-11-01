# fname = input("Enter file name or path: ")
fhand = open (r'C:\Users\hoand\Desktop\Programming\py files\files\Romeo.txt')

oldlist = []
newlist = []

for line in fhand:
    line = line.rstrip()
    words = line.split()
    oldlist.append(words)


# if "But" in oldlist[0]:
#     print("True") # oldlist is composed of 4 lists, the first list is index 0, and contains "But" substring

# print(len(oldlist)) # when this is printed, output is 4. oldlist contains 4 lists

# print(len(oldlist[0])) # output is 8. there are 8 words in the first list at index zero

# oldlist = oldlist[0] + oldlist[1] + oldlist[2] + oldlist[3] # creates one single list with all the words, now all words in list can be iterated through


for check in oldlist:
    if check in newlist:
        continue
    else:
        newlist.append(check)

newlist.sort()
print(newlist)