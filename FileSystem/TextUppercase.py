# Use words.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
reading = fh.read()

for ioOut in reading:
    #ioIn = ioOut.rstrip()
    print(ioOut.upper())