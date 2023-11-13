fhand = open(r'C:\Users\hoand\Desktop\Programming\PY4E Notes and Practice\files\Romeo.txt')

fhandread = fhand.read()
wordlist = fhandread.split()

count = {}

for words in wordlist:
    count[words] = count.get(words, 0) + 1

print(count)
