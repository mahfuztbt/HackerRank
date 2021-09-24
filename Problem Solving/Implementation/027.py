#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter 
#
# Complete the 'pickingNumbers' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#

def pickingNumbers(a):
    # Write your code here
    arr = Counter(a)
    maxnum = 0
    
    for i in range(100):
        maxnum = max(maxnum, arr[i]+arr[i+1])
        
    return maxnum

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = pickingNumbers(a)

    fptr.write(str(result) + '\n')

    fptr.close()
