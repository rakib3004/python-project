#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the solve function below.
def solve(s):


    names = list()
    names = s.split()
    n=len(names)
    fullName=''

    for name in names:
        #print(name)
        firstName = str(name)
        first=firstName.capitalize()
        #print(first)
        fullName=fullName+first+'.'

    return fullName

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()


    n=0
    result = solve(s)

    for r in result:
        if(r!='.'):
            print(r,end='')
        else:
            for k in range(n,len(s)):
                if (s[k] == ' '):
                    print(s[k])
                else:
                    n=k+1
                break



    print(result)
    #fptr.write(result + '\n')

    #fptr.close()
