# Enter your code here. Read input from STDIN. Print output to STDOUT

if __name__ == "__main__":
    present = list(map(int,input().split()))
    x = present[0]
    print(eval(input()) == present[1])