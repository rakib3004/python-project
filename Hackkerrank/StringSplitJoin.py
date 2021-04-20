def split_and_join(line):
    aList = list()
    aList = line.split()
    bStr=''
    for j in aList:
        aT = str(j)+'-'
        bStr=bStr+aT

    cStr = bStr[:len(bStr)-1]
    return  cStr

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)