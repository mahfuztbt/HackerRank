# Enter your code here. Read input from STDIN. Print output to STDOUT
input()
happiness = 0
array = list(map(int, input().split()))
A = set(map(int, input().split()))
B = set(map(int, input().split()))

for i in array:
    if i in A:
        happiness += 1
    elif i in B:
        happiness -= 1
        
print(happiness)