"""
URL of problem :- https://www.hackerrank.com/challenges/cut-the-sticks/problem

"""

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the cutTheSticks function below.
def cutTheSticks(arr):
    ans = []
    arr.sort(reverse = True)
    while len(arr) != 0:
        
        min_arr = min(arr)
        print(min_arr)
        count = 0
        print(arr)
        for i in range(len(arr)):
            if (arr[i] - min_arr) !=0:
                arr[i] = arr[i] - min_arr
                count +=1
            else:
                arr[i] = arr[i] - min_arr
                count +=1
        if len(arr) != 0:
            ans.append(count)
        arr = list(filter(lambda a: a != 0, arr))
        
    print(ans)
    return ans

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = cutTheSticks(arr)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
