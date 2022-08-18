#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'pickingNumbers' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#

def pickingNumbers(a):
    # Write your code here
    a.sort()
    arr = []
    for i in range(len(a)):
        sub_set = []
        sub_set.append(a[i])
        for j in range(i+1,len(a)):
            if a[j]-a[i] <= 1:
                sub_set.append(a[j])
        if len(sub_set) > 1:
            arr.append(sub_set)
    

    a = [len(i) for i in arr ]
    return max(a)
                                                                                                                                                                                                                                                                            

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = pickingNumbers(a)

    fptr.write(str(result) + '\n')

    fptr.close()
                                                                                                                                                                                                 
