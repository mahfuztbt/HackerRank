#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'surfaceArea' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY A as parameter.
#

def surfaceArea(A):
    # Write your code here
    
    n_rows = len(A)
    n_cols = len(A[0])
    total = (n_rows * n_cols) * 2 
    for row_i in range(n_rows): 
        for col_i in range(n_cols): 
            val = A[row_i][col_i]

            
            if row_i - 1 < 0:
                prev_row_val = 0
            else:
                prev_row_val = A[row_i - 1][col_i]

            total += abs(val - prev_row_val)

         
            if col_i - 1 < 0:
                prev_col_val = 0
            else: 
                prev_col_val = A[row_i][col_i - 1]
            total += abs(val - prev_col_val)

                     
            if col_i == n_cols - 1:
                total += val

        
        if row_i == n_rows - 1:
            total += sum(A[row_i])

    return total
    
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    H = int(first_multiple_input[0])

    W = int(first_multiple_input[1])

    A = []

    for _ in range(H):
        A.append(list(map(int, input().rstrip().split())))

    result = surfaceArea(A)

    fptr.write(str(result) + '\n')

    fptr.close()
