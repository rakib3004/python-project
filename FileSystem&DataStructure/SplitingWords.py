fname = input("Enter file name: ")
fh = open(fname)
lst = list()
totalList =list()
for line in fh:
    line.rstrip()
    lst = line.split()
    totalList = totalList+lst
totalList.sort()

iList=list()
for iLine in range(len(totalList)):
    iList.append(totalList[iLine])

print(iList)
