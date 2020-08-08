#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    N = int(input())


    Patterns = r"@gmail\.com$"
    RegEx = re.compile(Patterns)

    firstNamesList = []

    for N_itr in range(N):
        firstNameEmailID = input().split()

        firstName = firstNameEmailID[0]

        emailID = firstNameEmailID[1]

        if RegEx.search(emailID):
            firstNamesList.append(firstName)

    firstNamesList.sort()

    for name in firstNamesList:
        print(name)
