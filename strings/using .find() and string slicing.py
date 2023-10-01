def findwebsitename(data):

    findwebsitename = data[data.find("w.") + 2 : data.find(".co")]
    return findwebsitename
    
    
print(findwebsitename("https://www.wanikani.com/"))
print(findwebsitename("https://www.doordash.com/"))
print(findwebsitename("https://www.youtube.com/watch?v=mSDmr86MdHw"))


text = "X-DSPAM-Confidence:    0.8475"

findtext = text.find(" ")
findtext = text[findtext:]
findtext = float(findtext)
print(findtext)