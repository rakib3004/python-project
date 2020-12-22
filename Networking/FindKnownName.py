
from  urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl


iO='https://rakib3004.github.io'

def parsename(inputList):
    pos = int(inputList[1])
    if pos ==7:
        return inputList
    else :
        pos=pos+1
        createDefaultContext = ssl.create_default_context()
        createDefaultContext.check_hostname = False
        createDefaultContext.verify_mode = ssl.CERT_NONE

        html = urlopen(inputList[0], context=createDefaultContext).read()
        beautifulSoup = BeautifulSoup(html, "html.parser")
        inputList.clear()
        sum = 1
        selectPosition = 18
        iTags = beautifulSoup('a')
        for jTags in iTags:
            # print('TAG', jTags)
            if sum == selectPosition:
                iLink = str(jTags.get('href', None))
                inputList.append(inputList)
                inputList.append(pos)
                getIO = parsename(inputList)
                break
            else:
                a = 0  # print('URL  :', sum, jTags.get('href', None))
            sum = sum + 1
    return inputList

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
inputList = list()
sum=1
selectPosition=18
iTags = beautifulSoup('a')
for jTags in iTags:
    # print('TAG', jTags)
    if sum==selectPosition:
        iLink = str(jTags.get('href',None))
        inputList.append(inputList)
        inputList.append(1)
        inputList = parsename(inputList)
        break
    else:
       a=0 #print('URL  :', sum, jTags.get('href', None))
    sum =sum+1

print(inputList)
