# Enter your code here. Read input from STDIN. Print output to STDOUT

from collections import *
d = deque()

for i in range(int(input())):
    s = input().split()
    if s[0] == "append":
        d.append(s[1])
    elif s [0] == "pop":
        d.pop()
    elif s [0] == "appendleft":
        d.appendleft(s[1])
    else:
        d.popleft()
for i in d:
    print(i, end = " ")