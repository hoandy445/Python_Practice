try:
    fname = input("Enter file name here:")
    fhand = open(fname)

except:
    fhand = open(r"C:\Users\hoand\Desktop\Programming\PY4E Notes and Practice\files\regex_sampledata2.md")

import re
numlist = []

for line in fhand:
    line = line.rstrip()
    numbers = re.findall("[0-9]+",line)
    if len(numbers)>=1:
        for number in numbers:
            number = int(number)
            numlist.append(number)


print(sum(numlist))

#alternative
# numlist = []
# import re
# print( sum( [ int(x) for x in re.findall('[0-9]+',fhand.read()) ] ) )