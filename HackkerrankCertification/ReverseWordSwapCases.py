#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'reverse_words_order_and_swap_cases' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING sentence as parameter.
#

def reverse_words_order_and_swap_cases(sentence):
    #Write your code here
    ans = sentence.swapcase()
    #print(ans)

    listAns = ans.split()
    #print(listAns)

    wordI=""
    listAns.reverse()
    #print(listAns)
    lenL = len(listAns)

    for i in range(lenL):
        wordI = wordI+str(listAns[i])+" "

    sentence = wordI[:len(wordI)-1]
    return sentence

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    sentence = input()

    result = reverse_words_order_and_swap_cases(sentence)
    print(result)

    #fptr.write(result + '\n')

    #fptr.close()
