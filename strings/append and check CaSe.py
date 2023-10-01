# append

def append_middle(s1, s2):
    s3 = s1[:(len(s1)//2)]+ s2 + s1[len(s1)//2:]
    print(s3)


append_middle("Ault", "Kelly")


# print lower then upper


def lowerupper(str1):
    for i in str1:
        if i.islower():
            print(i, end="")

    for j in str1:
        if j.isupper():
            print(j, end="")

lowerupper("hElLo woRLd")

