#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'minimumDistances' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#

def minimumDistances(a):
    # Write your code here
    b = []
    c = []
    for i in range(len(a)):
        if a[i] not in c:
            c.append(a[i])
            for j in range(i+1, len(a)):
                if a[i] == a[j]:
                    b.append(abs(i-j))
            
    if len(b) == 0:
        return -1
    else:
        return min(b)
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = minimumDistances(a)

    fptr.write(str(result) + '\n')

    fptr.close()
