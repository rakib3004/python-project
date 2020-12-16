import  re
iFile = open('mbox-short')
numberList = list()

for iLoop in iFile:
    iLoop = iLoop.strip()
    iData = re.findall('^X-DSPAM-Confidence: ([0-9.]+)', iLoop)
    if len(iData)!=1 : continue
    number = float(iData[0])
    numberList.append(number)

print("MAximum",max(numberList))