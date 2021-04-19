import re

i = int(input())
t =0
for t in range(i):
    line = input()
    a,b = line.split();
    space = re.findall('^([(A-Z|a-z)])([A-Za-z0-9][.-_]){1,}@{1}[A-Za-z]+[A-Za-z]{1-3}',b)
    print(space)
    if(space!=[]):
        print(a,b)
    else:
        continue