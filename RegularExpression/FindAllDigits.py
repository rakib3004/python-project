import re

iTextFrom = open('minhas-cv')
iBigList = list()
for iLoop in iTextFrom:
    iPath = iLoop.strip()
    iList = re.findall('[0-9]+',iPath)
    iBigList.append(iList)

print(iBigList)