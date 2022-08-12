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
    max_v = 0
    max_s = scores[0]
    min_v = 0
    min_s = scores[0]
    scores.remove(scores[0])
    for score in scores:
        if max_s < score:
            max_v += 1
            max_s =score 
            
        if min_s > score:
            min_v += 1
            min_s = score 
    return max_v , min_v

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
