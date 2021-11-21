#!/bin/python3

import math
import os
import random
import re
import sys
from math import *

#
# Complete the 'encryption' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def encryption(s):
    # Write your code here
    n = len(s)
    r = floor(sqrt(n))
    c = ceil(sqrt(n))
    result = []
    
    for i in range(c):
        temp = []
        j = 0
        while i+j<n:
            temp.append(s[i+j])
            j+=c
        result.append("".join(temp))
    return " ".join(result)
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = encryption(s)

    fptr.write(result + '\n')

    fptr.close()
