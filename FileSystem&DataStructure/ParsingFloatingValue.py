# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
iCount=0
iSum =0.0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    else:
        iPos = line.endswith("X-DSPAM-Confidence:")
        iWord = line[iPos + 20:iPos+26]
        iWord=iWord.strip()
        iFloat = float(iWord)
        iCount=iCount+1
        iSum = iSum+iFloat

print('Average spam confidence:',iSum/iCount)