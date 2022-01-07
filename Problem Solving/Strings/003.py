#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'minimumNumber' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. STRING password
#

def minimumNumber(n, password):
    # Return the minimum number of characters to make the password strong
    spl = "!@#$%^&*()-+"
    l = [0,0,0,0]
    
    for char in password:
        if char.isdigit():
            l[0] = 1
        elif char.islower():
            l[1] = 1
        elif char.isupper():
            l[2] = 1
        elif char in spl:
            l[3] = 1
    
    return max(6 - len(password), 4 - sum(l))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    password = input()

    answer = minimumNumber(n, password)

    fptr.write(str(answer) + '\n')

    fptr.close()
