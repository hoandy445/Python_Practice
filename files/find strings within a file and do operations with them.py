# find all lines that start with "X-DSPAM-Confidence," add all the numbers and get an average
# for use with mailbox.txt 

filename = input("Enter file name or path: ")

try:
    fhand = open(filename)

except:
    print("File cannot be accessed.")
    quit()

linecount = 0
total = 0

for line in fhand:
    
    if line.startswith("X-DSPAM-Confidence"):
        colonpos = line.find(":")
        numpos = line[colonpos + 1:]
        numpos = float(numpos)
        total = total + numpos
        linecount = linecount + 1

print("Number of lines:", linecount)
print("Average spam confidence:", (total/linecount))


    

