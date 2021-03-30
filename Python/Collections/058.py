# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import namedtuple
(n, s_info) = (int(input()), input().split())
info = namedtuple("info", s_info)
l = [int(info._make(input().split()). MARKS) for i in range(n)]

print(sum(l)/len(l))