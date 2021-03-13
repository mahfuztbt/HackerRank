# Enter your code here. Read input from STDIN. Print output to STDOUT

if __name__ == "__main__":
    A = set(map(int, input().split()))
    n = int(input())
    output = True
    for i in range(n):
        B = set(map(int, input().split()))
        if (B.issubset(A) and len(A.difference(B)) > 0) == False:
            output = False
    print(output)