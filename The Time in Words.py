"""
URL of problem :- https://www.hackerrank.com/challenges/the-time-in-words/problem

"""

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the timeInWords function below.
def timeInWords(h, m):
    t = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'eleven', 'twelve', 'thirteen', 'fourteen','fifteen','sixteen','seventeen','eighteen','nineteent','twenty', 'twenty one', 'twenty two','twenty three', 'twenty four', 'twenty five', 'twenty six', 'twenty seven', 'twenty eight', 'twenty nine']

    if m == 00:
        print('a')
        return str(t[h-1]) + " o' clock"
    elif h == 0 and m == 00:
        return "zero o' clock"
    elif m == 1:
        return str(t[m-1]) + " minute past " + str(t[h-1])
    elif m > 1 and m <15:
        return str(t[m-1]) + " minutes past " + str(t[h-1])
    elif m == 15:
        return "quarter past " + str(t[h-1])
    elif m > 15 and m < 30:
        return str(t[m-1]) + " minutes past " + str(t[h-1])
    elif m == 30:
        return "half past " + str(t[h-1])
    elif m == 45:
        return "quarter to " + str(t[h])
    elif m > 30:
        m = 60 - m
        print(m)
        return str(t[m-1]) + " minutes to " + str(t[h])
    


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    h = int(input())

    m = int(input())

    result = timeInWords(h, m)

    fptr.write(result + '\n')

    fptr.close()
