fruit = "banana"


def reversestr(s):
    reverse = ""
    
    for i in s:
        reverse = i + reverse
    return(reverse)


print(reversestr(fruit))
    

def reversestr2(s):
    i = len(s)

    while i >= 0:
        i = i - 1
        print(s[i])

reversestr2(fruit)


        