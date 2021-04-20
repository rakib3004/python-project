a=int(input())
b=2*(2*(a-1))+1

for i in range(1,a+1):
    if((i-1)*2+1<=a):
        c=4*i-3
        k=int((b-c)/2)
        for j in range(k):
            print('-', end='')
        t=96
        tt=c
        for j in range(1,c+1):
            if(j%2==0):
                print('-', end='')
            elif((j-1)*2+1<=c):
                print(chr(t+tt))
                tt=tt-1
            elif((j-1)*2+1>c):
                print(chr(t + tt))
                tt = tt + 1
        for j in range(k):
            print('-', end='')
    else:
        i1=(a+1)-i
        c = 4 * i1 - 3
        k = int((b - c) / 2)
        for j in range(k):
            print('-', end='')
        t = 96
        tt = c
        for j in range(1, c + 1):
            if (j % 2 == 0):
                print('-', end='')
            elif ((j - 1) * 2 + 1 <= c):
                print(chr(t + tt))
                tt = tt - 1
            elif ((j - 1) * 2 + 1 > c):
                print(chr(t + tt))
                tt = tt + 1
        for j in range(k):
            print('-', end='')
    print()
