# Enter your code here. Read input from STDIN. Print output to STDOUT

a = int(input())
b = list(map(int, input().split()))
s = set()
t = set()
for i in b:
    if i not in s:
        s.add(i)
        t.add(i)
    else:
        t.discard(i)
print(t.pop())