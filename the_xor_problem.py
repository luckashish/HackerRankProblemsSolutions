"""
URL problem : https://www.hackerrank.com/contests/hack-the-interview-v-asia-pacific/challenges/the-xor-problem

"""
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'maxXorValue' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING x
#  2. INTEGER k
#

def maxXorValue(x, k):
    # Write your code here
    ans = ''
    for i in x:
        if k > 0:
            if '0' == i:
                ans += '1'
                k -= 1
            else:
                ans += '0'
        else:
            ans += '0'
    return ans
                

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        s = input()

        k = int(input().strip())

        y = maxXorValue(s, k)

        fptr.write(y + '\n')

    fptr.close()
