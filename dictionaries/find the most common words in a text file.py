fhand = open(r"C:\Users\hoand\Desktop\Programming\PY4E Notes and Practice\files\random article.txt")
fhandread = fhand.read()
fhandread = fhandread.split()

count = {}

for word in fhandread:
    count[word] = count.get(word,0) + 1

maxvalue = None
maxkey = None

# for key in count:
#     if maxvalue is None:
#         maxvalue = count[key]
#     elif count[key] > maxvalue:
#         maxkey = key
#         maxvalue = count[key]

#print("The most common word is:", '"' + maxkey + '",', "which occurs", maxvalue, "times.")


# or:

for key,value in count.items():
    if maxvalue is None or value > maxvalue:
        maxkey = key
        maxvalue = value

print(maxkey,maxvalue)







