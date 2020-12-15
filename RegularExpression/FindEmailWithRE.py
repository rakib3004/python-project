import re

jFile = open('mbox-short')
emailBox = list()
for iteratorLine in jFile:
    iteratorLine = iteratorLine.strip()
    getEmail = re.findall('\S+@\S+',iteratorLine)
    #print(getEmail)
    emailBox.append(getEmail)

#print whole list of email name
print(emailBox)