import urllib.request, urllib.parse, urllib.error

iWebText = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')

countWord = dict()
for iLoop in iWebText:
    packetParse = iLoop.decode().split()
    for iPacket in packetParse:
        countWord[iPacket] = countWord.get(iPacket,0)+1

print(countWord)