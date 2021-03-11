# Enter your code here. Read input from STDIN. Print output to STDOUT

from itertools import permutations

s, n = input().split()
s = sorted(s)
n = int(n)

for i in list(permutations(s,n)):
    print("".join(i))