# Enter your code here. Read input from STDIN. Print output to STDOUT

from collections import Counter

n = int(input())

stock = list(map(int, input().split(" ")))
dict = Counter(stock)

p =0
k = int(input())
for i in range(k):
    size, price = map(int, input().split())
    if dict[size]:
        dict[size]-=1
        p=p+price

print(p)

