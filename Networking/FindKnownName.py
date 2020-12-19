
from  urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl



#ignore SSl certificate errors
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
pos=1
count=1
selectPosition=18
iTags = beautifulSoup('a')
for jTags in iTags:
    # print('TAG', jTags)
    if sum==selectPosition:
       print('URL :',sum,jTags.get('href',None))
       sum =sum+1
    # print('Contents:',jTags.contents[0])
#     sum =sum+int(jTags.contents[0])
#
# print(sum)
