# Enter your code here. Read input from STDIN. Print output to STDOUT

from itertools import combinations
s, n = input().split()
for i in range(1, int(n)+1):
    a = list(combinations(sorted(s), i))
    for j in a:
        print("".join(j))