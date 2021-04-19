import  re

n = int(input())
i =0
for i in range(n):
    iNumber = str(input())
    i10 = len(iNumber)
    iF = re.findall('^(7|8|9)', iNumber)
    #print(iF)
    if(iF==[]):
        print('NO')
    else:
        if(i10==10):
            print('YES')






