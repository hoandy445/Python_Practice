# fhand = open(r"C:\Users\hoand\Desktop\Programming\PY4E Notes and Practice\files\mailbox.txt")

# count = {}
# for line in fhand:
#     if not line.startswith("From "): continue
#     else:
#         line = line.split()
#         email = line[1]
#         count[email] = count.get(email,0) + 1

# keyvalue = []
# for k,v in count.items():
#     keyvalue.append((v,k))

# keyvalue.sort(reverse=True)

# for v,k in keyvalue[:1]:
#     print(k,v)

# count = {}
# for line in fhand:
#     if line.startswith("From "):
#         line = line.split()
#         time = line[5].split(":")
#         hour = time[0]
#         count[hour] = count.get(hour,0) + 1

# for k,v in sorted(count.items()):
#     print(k,v)

fhand = open(r"C:\Users\hoand\Desktop\Programming\PY4E Notes and Practice\files\Romeo.txt")
import string
count = {}
for line in fhand:
    line = line.translate(line.maketrans("","",string.punctuation))
    line = line.rstrip()
    line = line.lower()
    for letter in line:
        if letter == " ":
            continue
        count[letter] = count.get(letter,0) + 1

kv = []
for k,v in count.items():
    kv.append((v,k))

kv.sort(reverse=True)
for v,k in kv:
    print(k,v)


