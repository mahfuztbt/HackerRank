#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input())
    a = list(bin(n))
    a = a[2:]

    b = 0
    mx = 0
    for i in range(len(a)):
        if a[i] == "1":
            b += 1
        else:
            if mx <b:
                mx = b
            b = 0
    if mx < b:
        print(b)
    else:
        print(mx)

