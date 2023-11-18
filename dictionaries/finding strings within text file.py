try:
    filename = input("Enter file name: ")
    fhand = open(filename)

except:
    print("File could not be accessed. Closing program...")
    quit()


emails = {}

for line in fhand:
    if len(line) < 3:
        continue
    elif line.startswith("From "):
        line = line.split()
        email = line[1]
        emails[email] = emails.get(email, 0) + 1

commonemail = None

for key,value in emails.items():
    if commonemail is None or value > commonemail:
        commonemailname = key
        commonemail = value

print(commonemailname, commonemail)
        