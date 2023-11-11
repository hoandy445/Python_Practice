fname = input("Enter file name or path: ")
fhand = open(fname)

count = 0

for line in fhand:
    if line.startswith("From:"):
        continue
    elif line.startswith("From"):
        line = line.split()
        email = line[-1]
        count = count + 1
        print(email)

print("There were", count, "lines in the file with From as the first word")