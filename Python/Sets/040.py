# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
l = set(map(int, input().split()))
rep = int(input())
for i in range(rep):
    sr, num = input().split()
    l2 = set(map(int, input().split()))
    eval("l.{0}({1})".format(sr, l2))
    
print(sum(l))