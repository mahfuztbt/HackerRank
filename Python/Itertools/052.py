# Enter your code here. Read input from STDIN. Print output to STDOUT

from itertools import combinations_with_replacement

s, n = input().split(" ")
for i in list(combinations_with_replacement(sorted(s), int(n))):
    print("".join(i))