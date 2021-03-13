# Enter your code here. Read input from STDIN. Print output to STDOUT

for i in range(int(input())):
    a = int(input()); 
    A = set(input().split()) 
    b = int(input());
    B = set(input().split())
    print(A.issubset(B))