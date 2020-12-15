import re

iFile = open('mbox-short')

for line in iFile:
    iLine = line.strip()
    if re.search('From:', iLine):
        print(iLine)