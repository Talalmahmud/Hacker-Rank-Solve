#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'cavityMap' function below.
#
# The function is expected to return a STRING_ARRAY.
# The function accepts STRING_ARRAY grid as parameter.
#

def cavityMap(grid):
    # Write your code here
    grid_length = len(grid)
    matrix = []
    for i in grid:
        l = []
        for j in i:
            l.append(j)
        matrix.append(l)
    
    for i in range(1,grid_length-1):
        for j in range(1,grid_length-1):
            left = matrix[i][j-1]
            right = matrix[i][j+1]
            top = matrix[i-1][j]
            bottom = matrix[i+1][j]
            max_value = max(left, right, top, bottom)
            if matrix[i][j] > max_value:
                matrix[i][j] = 'X'
    grid = []
    for i in matrix:
        l = ''
        for j in i:
            l += j
        grid.append(l)
    return grid
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    grid = []

    for _ in range(n):
        grid_item = input()
        grid.append(grid_item)

    result = cavityMap(grid)

    fptr.write('\n'.join(result))
    fptr.write('\n')

    fptr.close()
