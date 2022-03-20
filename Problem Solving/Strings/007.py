#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'separateNumbers' function below.
#
# The function accepts STRING s as parameter.
#

def separateNumbers(s):
    # Write your code here
    if len(s) == 1:
        print("NO")
        return 
    else:
        for i in range(1, len(s)//2 + 1):
            genstr = s[:i]
            prev = int(genstr)
            
            
            while len(genstr) < len(s):
                next = prev + 1
                genstr = genstr + str(next)
                prev = next
            
            if genstr == s:
                print("YES", s[:i])
                return 
        print("NO")

if __name__ == '__main__':
    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        separateNumbers(s)
