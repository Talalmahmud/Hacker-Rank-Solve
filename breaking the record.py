#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'breakingRecords' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY scores as parameter.
#

def breakingRecords(scores):
    # Write your code here
    length = len(scores)
    max_value = min_value = scores[0]
    max_count =0
    min_count = 0
    for i in range(1, length):
        if max_value < scores[i]:
            max_count += 1
            max_value = scores[i]
        
        if min_value > scores[i]:
            min_count += 1
            min_value = scores[i]
    return [max_count, min_count]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    scores = list(map(int, input().rstrip().split()))
    
    result = breakingRecords(scores)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
