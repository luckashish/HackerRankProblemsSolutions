"""
URL of problem :- https://www.hackerrank.com/challenges/breaking-best-and-worst-records/problem

"""

# My Solution

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the breakingRecords function below.
def breakingRecords(scores):
    h_score = [scores[0]]
    l_score = [scores[0]]
    for i in range(1,len(scores)):
        if scores[i] > h_score[i-1]:
            h_score.append(scores[i])
        else:
            h_score.append(h_score[i-1])
        if scores[i] < l_score[i-1]:
            l_score.append(scores[i])
        else:
            l_score.append(l_score[i-1])
    print(l_score, h_score)
    mi = l_score[0]
    mx = h_score[0]
    countmin = 0
    countmax = 0
    for j in range(len(scores)):
        
        if mi > l_score[j]:
            mi = l_score[j]
            countmin += 1
        if mx < h_score[j]:
            mx = h_score[j]
            countmax +=1

    return [countmax,countmin]



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
