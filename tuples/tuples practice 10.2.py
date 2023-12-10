fhand = open(r"C:\Users\hoand\Desktop\Programming\PY4E Notes and Practice\files\mailbox.txt")

count = {}
for line in fhand:
    if line.startswith("From "):
        line = line.split()
        time = line[5].split(":")
        hour = time[0]
        count[hour] = count.get(hour,0) + 1

for k,v in sorted(count.items()):
    print(k,v)