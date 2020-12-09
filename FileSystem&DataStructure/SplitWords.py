fname = input("Enter file name: ")
fh = open(fname)
lst = list()
item = list()
totalList =list()
for line in fh:
    line.rstrip()
    item.append('a')
    lst = line.split()
    totalList = totalList+lst
totalList.sort()

iList=set()
for iLine in range(len(totalList)):
    iList.add(totalList[iLine])


iTopList =list()
iTopList=list(iList)
iTopList.sort()

print(iTopList)
