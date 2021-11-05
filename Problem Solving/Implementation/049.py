#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'queensAttack' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER k
#  3. INTEGER r_q
#  4. INTEGER c_q
#  5. 2D_INTEGER_ARRAY obstacles
#

def queensAttack(n, k, r_q, c_q, obstacles):
    # Write your code here
    total = 0
    obs = {}
    
    for i, j in obstacles:
        if i in obs:
            obs[i][j] = 1
        else:
            obs[i] = {j:1}
            
    def limit(x, y):
        return True if 1<=x<=n and 1<=y<=n else False
    
    def check(x, y, xi, yi):
        count = 0
        x+=xi
        y+=yi
        while limit(x,y) and obs.get(x,{}).get(y,0)==0:
            count+=1
            x+=xi
            y+=yi
        return count
    
    r = [0,0,-1,1,-1,1,-1,1]
    c = [1,-1,0,0,-1,1,1,-1]
    
    for i, j in zip(r,c):
        total+= check(r_q, c_q, i, j)
    return total

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    second_multiple_input = input().rstrip().split()

    r_q = int(second_multiple_input[0])

    c_q = int(second_multiple_input[1])

    obstacles = []

    for _ in range(k):
        obstacles.append(list(map(int, input().rstrip().split())))

    result = queensAttack(n, k, r_q, c_q, obstacles)

    fptr.write(str(result) + '\n')

    fptr.close()
