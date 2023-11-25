try:
    fname = input("Enter file name: ")
    fhand = open(fname)

except: 
    fhand = open(r"C:\Users\hoand\Desktop\Programming\PY4E Notes and Practice\files\mailbox.txt")

count = {}

# for line in fhand:
#     line = line.rstrip()
#     if not line.startswith("From "): continue
#     else:
#         line = line.split()
#         count[line[2]] = count.get(line[2],0) + 1

for line in fhand:
    line = line.rstrip()
    if not line.startswith("From "): continue
    else:
        line = line.split()
        email = line[1].split("@")
        email = email[1]
        count[email] = count.get(email,0) + 1

maxval = None
maxkey = None 

for key,value in count.items():
    if maxval is None or value > maxval:
        maxval = value
        maxkey = key

print(count)
print(maxkey,maxval)
