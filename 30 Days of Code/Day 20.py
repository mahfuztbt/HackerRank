#!/bin/python3

import sys

n = int(input().strip())
a = list(map(int, input().strip().split(' ')))
# Write Your Code Here
totalNumberOfSwaps = 0
for i in range(n):
    numberOfSwaps = 0
    for j in range(n - 1):
        if a [j] > a[j+1]:
            temp = a[j]
            a[j] = a[j + 1]
            a[j + 1] = temp
            numberOfSwaps  += 1
    totalNumberOfSwaps += numberOfSwaps

    if numberOfSwaps == 0:
        break

print("Array is sorted in " + str(totalNumberOfSwaps) + " swaps. ")
print("First Element: " + str(a[0]))
print("Last Element: " + str(a[n-1]))
