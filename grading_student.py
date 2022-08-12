#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'gradingStudents' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY grades as parameter.
#

def gradingStudents(grades):
    # Write your code here
    n_grade = []
    for grade in grades:
        m = grade % 5
        n = grade + (5-m)
        if n - grade < 3:
            if n >= 40:
                n_grade.append(n)
            else:
                n_grade.append(grade)
        elif n - grade == 3:
            n_grade.append(grade)
        else:
            n_grade.append(grade)
            
            
    return n_grade
            

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    grades_count = int(input().strip())

    grades = []

    for _ in range(grades_count):
        grades_item = int(input().strip())
        grades.append(grades_item)

    result = gradingStudents(grades)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
