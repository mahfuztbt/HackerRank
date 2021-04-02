# Enter your code here. Read input from STDIN. Print output to STDOUT

from collections import OrderedDict
n = int(input())
d = OrderedDict()
for i in range(n):
    item, space, number = input().rpartition(" ")
    number = int(number)
    if item in d.keys():
        d[item] += number 
    else:
        d[item] = number
for i in d.keys():
    print(i, d[i])