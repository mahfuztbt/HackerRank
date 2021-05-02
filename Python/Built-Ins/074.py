# Enter your code here. Read input from STDIN. Print output to STDOUT

n = int(input())
l = input().split()

print(all(int(i) > 0 for i in l) and any( j == j[::-1] for j in l))