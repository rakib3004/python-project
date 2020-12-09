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

iPoint =1
for iterIO in range(len(iList)):
    if(iPoint== 1):
        print(iList[iterIO])
        iPoint= 2
    else:
        iPoint=1


print("There were", int(count/2), "lines in the file with From as the first word")
