"""
URL of problem :- https://www.hackerrank.com/challenges/migratory-birds/problem

"""

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the migratoryBirds function below.
def migratoryBirds(arr):
    arr_set = set(arr)
    arr_dic = dict()
    for bird in arr_set:
        arr_dic[bird] = arr.count(bird)
    key_max = max(arr_dic.keys(), key = (lambda k:arr_dic[k]))
    return key_max



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = migratoryBirds(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
