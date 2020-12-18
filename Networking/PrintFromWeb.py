import urllib.request, urllib.parse, urllib.error

iWebText = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')

for iLoop in iWebText :
    print(iLoop.decode().strip())

