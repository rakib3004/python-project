import urllib.request
import re
url = urllib.request.urlopen('http://py4e-data.dr-chuck.net/regex_sum_1081148.txt')
sum=0
intList = list()
for jterator in url:
    iterator = str(jterator)
    intList.append(iterator)
    # iterator = iterator.decode('uft-8')
    intFile = re.findall('[0-9]+', iterator)
    for itFile in intFile:
       number = int(itFile)
       # print(number)
       sum = sum+number

print('sum:', sum)
# for iLoop in intList:
#     print('---->',iLoop)