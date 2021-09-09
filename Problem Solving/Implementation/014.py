#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'getTotalX' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER_ARRAY b
#

def getTotalX(a, b):
    # Write your code here
    multiples_a = []
    multiples_b = []
    factors_b = []
    final_integers = []
    total_length = len(a+b)
    
    for i in range(1,101):
        for number_a in a:
            if i%number_a == 0:
                multiples_a.append(i)
        for number_b in b:
            if number_b % i == 0:
                factors_b.append(i)
        potential_intergers = multiples_a + factors_b
    for number in potential_intergers:
        if potential_intergers.count(number) == total_length:
            final_integers.append(number)
    return len(set(final_integers))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    brr = list(map(int, input().rstrip().split()))

    total = getTotalX(arr, brr)

    fptr.write(str(total) + '\n')

    fptr.close()
