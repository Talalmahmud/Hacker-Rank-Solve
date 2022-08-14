#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def miniMaxSum(arr):
    # Write your code here
    new_arr = []
    for i in range(len(arr)):
        t = arr[i]
        arr[i]=0
        new_arr.append(sum(arr))
        arr[i] = t
    print(f"{min(new_arr)} {max(new_arr)}")
        
        

if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
