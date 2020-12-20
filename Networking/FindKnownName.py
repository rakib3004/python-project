
from  urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

pos=1
iO='https://rakib3004.github.io'

def parsename(inputURL):
    if pos ==7:
        return iO
    else :
        pos=pos+1
        createDefaultContext = ssl.create_default_context()
        createDefaultContext.check_hostname = False
        createDefaultContext.verify_mode = ssl.CERT_NONE

        html = urlopen(inputURL, context=createDefaultContext).read()
        beautifulSoup = BeautifulSoup(html, "html.parser")

        sum = 1
        selectPosition = 18
        iTags = beautifulSoup('a')
        for jTags in iTags:
            # print('TAG', jTags)
            if sum == selectPosition:
                iLink = str(jTags.get('href', None))
                getIO = parsename(iLink)
                break
            else:
                a = 0  # print('URL  :', sum, jTags.get('href', None))
            sum = sum + 1
    return getIO

#ignore SSl certificate errors
pos=1
createDefaultContext = ssl.create_default_context()
createDefaultContext.check_hostname = False
createDefaultContext.verify_mode =ssl.CERT_NONE

inputURL = input('Enter URL:')
html = urlopen(inputURL,context=createDefaultContext).read()
beautifulSoup = BeautifulSoup(html, "html.parser")
# intCount = int(input('Enter Count:'))
# intPosition = int(input('Enter Position:'))
#Retrive all of the anchor tags
sum=1
selectPosition=18
iTags = beautifulSoup('a')
for jTags in iTags:
    # print('TAG', jTags)
    if sum==selectPosition:
        iLink = str(jTags.get('href',None))
        getIO = parsename(iLink)
        break
    else:
       a=0 #print('URL  :', sum, jTags.get('href', None))
    sum =sum+1

print(getIO)
