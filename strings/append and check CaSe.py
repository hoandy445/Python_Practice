# append

def append_middle(s1, s2):
    s3 = s1[:(len(s1)//2)]+ s2 + s1[len(s1)//2:]
    print(s3)


append_middle("Ault", "Kelly")


# print lower then upper

str1 = "PyNaTive"

for i in str1:
    if i.islower():
        print(i, end="")
    else:
        continue

for j in str1:
    if j.isupper():
        print(j, end="")

