#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))
    r = 0

    # Write your code here
    for i in range(n):
        numberofSwaps = 0
        
        for j in range(n-1):
            if a[j] > a[j+1]:
                t = a[j]
                a[j] = a[j+1]
                a[j+1] = t
                numberofSwaps += 1
                if numberofSwaps != 0:
                    r += 1
        if numberofSwaps == 0:
            break
    
    print(f"Array is sorted in {r} swaps.")
    print(f"First Element: {a[0]}")
    print(f"Last Element: {a[len(a)-1]}")
