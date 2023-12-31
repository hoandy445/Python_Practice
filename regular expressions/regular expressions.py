#more text parsing practice, this time with regex. pulls characters lines and appends them into a corresponding list. 
#code is kind of a mess, but it does what it's supposed to do
script = open(r"C:\Users\hoand\Desktop\Programming\PY4E Notes and Practice\files\acting script.txt")
import re

narrator = []
sheldrake = []
bud = []
switch = True

for line in script:
    findline = re.findall("^[a-zA-Z]+",line)
    if len(findline) > 0:
        narrator.append(line)
    else: 
        line = line.strip()
        if re.search("SHELDRAKE",line) is not None:
            switch = True; continue
        elif re.search("BUD", line) is not None:
            switch = False; continue
        if switch == True and len(line)>0:
            sheldrake.append(line)
        elif switch == False and len(line)>0:
            bud.append(line)


        
       
    
            

