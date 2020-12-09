iFile = input('Enter the file name')
file = open(iFile)

iCountWords = dict()

for iItem in file:
    iText = iItem.split()
    for jItem in iText:
        iCountWords[jItem]=iCountWords.get(jItem,0)+1

for iKey, iItem in iCountWords.items():
    print(iKey,iItem)