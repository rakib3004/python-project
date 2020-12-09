fname = input("Enter file name: ")
if len(fname) < 1 : fname = "mbox-short.txt"

fh = open(fname)
count = 0
iList= list()

for iFile in fh:
    if iFile.startswith('From'):
        strLine = iFile.split()
        iList.append(strLine[1])
        count= count+1
newList=list()
iPoint =1
iEmail = dict()

for iterIO in range(len(iList)):
    if(iPoint== 1):
        iPoint= 2
    else:
        iPoint=1

for iIter in iList:
    if (iPoint == 1):
        iPoint = 2
        #print(iList[iterIO])
        iEmail[iIter]=iEmail.get(iIter,0)+1
    else:
        iPoint = 1

bigCount =None
bigWord = None
jCount =0
for iIter in iEmail:
        #print(iList[iterIO])
        jCount = iEmail[iIter]
        if bigCount is None or jCount>bigCount:
            bigWord = iIter
            bigCount = jCount


print(bigWord,bigCount)