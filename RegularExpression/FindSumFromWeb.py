import urllib.request
import  re
url = urllib.request.urlopen('http://py4e-data.dr-chuck.net/regex_sum_42.txt')
sum=0
for iterator in url:
    intFile = re.findall('[0-9]+', iterator)
    for itFile in intFile:
         number = int(itFile)
         sum = sum+number

print('sum:', sum)

