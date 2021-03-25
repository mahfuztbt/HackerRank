# Enter your code here. Read input from STDIN. Print output to STDOUT


from itertools import product

t, m = map(int, input().split())
l = [list(map(int, input().split()))[1:] for i in range(t)]

print(max(map(lambda x: sum(i**2 for i in x)%m, product(*l))))
