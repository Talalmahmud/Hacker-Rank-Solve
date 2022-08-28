#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'equalizeArray' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def equalizeArray(arr):
    # Write your code here
    
    arr1 = {}
    a = []
    for i in arr:
        if i not in a:
            arr1[i] = arr.count(i)
            a.append(i)
    arr1.pop(max(arr1, key=arr1.get))
    c = 0
    for i,k in arr1.items():
        c += arr1[i]
    return c
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = equalizeArray(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
