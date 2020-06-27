"""
URL :- https://www.hackerrank.com/contests/hack-the-interview-v-asia-pacific/challenges/candy-crush-4
"""
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'getMaxScore' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING jewels as parameter.
#

def getMaxScore(jewels):
    # Write your code here
    # Write your code here
    temp_list = [jewels[0]]
    count = 0
    for jewel in jewels[1:]:
        if len(temp_list) != 0 and temp_list[-1] == jewel:
            while len(temp_list) != 0 and temp_list[-1] == jewel:    
                temp_list.pop()
                count += 1
        else:
            temp_list.append(jewel)
    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        jewels = input()

        ans = getMaxScore(jewels)

        fptr.write(str(ans) + '\n')

    fptr.close()
