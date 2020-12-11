name = input("Enter file:")
if len(name) < 1 : name = "mbox-short"
iRead = open(name)
iInt=1
iThings = dict()
for iLoop in iRead :
    if iLoop.startswith('From'):
        if iLoop.find('@') and iLoop.find('2008'):
            if iInt == 1:
                iWords = iLoop.split()
                iInt = 2
                iGot = iWords[5]
                iGet = iGot[:2]
                iThings[iGet] = iThings.get(iGet, 0)+1
            else:
                iInt = 1
                continue

aList = list()
for a,b in iThings.items():
    iTruples = (a, b)
    aList.append(iTruples)

aList = sorted(aList ,reverse=False)

for c,f in aList:
    print(c,f)