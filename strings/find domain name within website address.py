web1 = "https://jisho.org/"
web2 = "https://www.youtube.com/watch?v=AmIK3qOTcoI"
web3 = "https://mail.google.com/mail/"


def findweb(website):
    # the amount of periods in website addresses can vary, which can be counted with a loop and accounted for
    howmanyperiods = 0
    for x in website:
        if x == ".":
            howmanyperiods = howmanyperiods + 1

    if howmanyperiods == 1:

        pos1 = website.find("/") # find the position of the first slash
        pos1 = pos1 + 2 # set pos1 as the position after the two slashes, we're at the first letter after the slashes, which is going to be either the actual name of the website, or the subdomain name (www., mail., blog., etc.)
        
        pos2 = website.find(".", pos1) # find the first period after the scheme ("https://") and after pos1
        webname = website[pos1 : pos2]
        return(webname)

    else:

        pos1 = website.find(".") # find position of first period after the subdomain name
        pos1 = pos1 + 1 # set position after the period

        pos2 = website.find(".", pos1) # find position of the next period, this will check everything after pos1. we're trying to find the position of the period before the top-level domain (.com, .org, etc.)
        webname = website[pos1: pos2]
        return(webname)
        
print(findweb(web1))

