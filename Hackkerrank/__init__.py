import math
import os
import random
import re
import sys


if __name__ == '__main__':
    n = int(input().strip())
    if(n%2==0):
        if(n<=5&n>=2):
            print('Not Weird')
        elif(n<=20&n>=6):
            print('Weird')
        else:
            print('Not Weird')
    elif(n%2==1):
        print('Weird')

