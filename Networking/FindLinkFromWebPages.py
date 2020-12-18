
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

#Retrive all of the anchor tags

iTags = beautifulSoup('a')
for jTags in iTags:
    print('TAG', jTags)
    print('URL :',jTags.get('href',None))
    print('Contents:',jTags.contents[0])
    print('Attrs:', jTags.attrs)