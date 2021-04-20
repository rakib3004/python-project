s=str(input())
p,q = s.split()
a=int(p)
b=int(q)

for i in range(1,a+1):
    if((i-1)*2+1==a):
        k=int((b-7)/2)
        for j in range(k):
            print('-',end='')
        print('WELCOME',end='')
        for j in range(k):
            print('-',end='')
    elif(i<=int(a/2)):
        c=6*i-3
        k=int((b-c)/2)
        for j in range(k):
            print('-', end='')
        print('.', end='')
        print('|', end='')
        for j in range(3,c):
            if((j+1)%3==0):
                print('|', end='')
            else:
                print('.', end='')
        print('.', end='')
        for j in range(k):
            print('-', end='')
    else:
        i1=(a+1)-i
        c = 6 * i1 - 3
        k = int((b - c) / 2)
        for j in range(k):
            print('-', end='')
        print('.', end='')
        print('|', end='')
        for j in range(3, c):
            if ((j + 1) % 3 == 0):
                print('|', end='')
            else:
                print('.', end='')
        print('.', end='')
        for j in range(k):
            print('-', end='')
    print()
