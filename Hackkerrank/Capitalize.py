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
    firstName = str(names[0])
    lastName = str(names[1])
    firstName=firstName.capitalize()
    lastName=lastName.capitalize()

    return  firstName+" "+lastName

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()
