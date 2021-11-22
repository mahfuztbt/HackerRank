#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'biggerIsGreater' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING w as parameter.
#

def biggerIsGreater(w):
    # Write your code here
    result = ""
    n = len(w)
    w = list(w)
    
    i = n-2
    while i >= 0 and w[i] >= w[i+1]:
        i -= 1
    
    if i == -1:
        result = 'no answer'
    else:
        j = n-1
        while j>= i and w[j] <= w[i]:
            j -= 1
        w[i], w[j] = w[j], w[i]
        w = "".join(w)
        
        result = w[:i+1] + w[i+1:][::-1]
    return result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    T = int(input().strip())

    for T_itr in range(T):
        w = input()

        result = biggerIsGreater(w)

        fptr.write(result + '\n')

    fptr.close()
