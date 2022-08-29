#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'repeatedString' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. STRING s
#  2. LONG_INTEGER n
#

def repeatedString(s, n):
    # Write your code here
    s_list = [i for i in s]
    num_a = s_list.count('a')
    
    count_a = (n // len(s_list)) * num_a
    n = n % len(s_list)
    
    for i in range(n):
        if s_list[i] == 'a':
            count_a += 1
    return count_a
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    n = int(input().strip())

    result = repeatedString(s, n)

    fptr.write(str(result) + '\n')

    fptr.close()
