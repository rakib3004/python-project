name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)

iRead = handle.read()

for iLoop in iRead :
    if iLoop.startswith('From'):
        if iLoop.find('@') and iLoop.find(':'):
            iSentence = iLoop.strip()
            iWords = iSentence.split()
            iThings = iWords[4]


iCollector = dict()

for iDir in iThings:
    iCollector[iDir] = iCollector.get(iDir,0)+1


iList = list()

iList = iCollector.items()

iList = sorted(iList,reverse=False)

