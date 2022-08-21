#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c, k):
    n = len(c)
    e = 100
    i = 0
    on = False
    if c[0]==1:
        e -= 2
    while not on:
        i = (i+k)%n
        if i == 0:
            on = True
            e -= 1
        else:
            if c[i] == 1:
               e -= 3
            else:
               e -= 1
        print(e)
               
    return e
       

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c, k)

    fptr.write(str(result) + '\n')

    fptr.close()
