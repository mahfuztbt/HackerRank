# Enter your code here. Read input from STDIN. Print output to STDOUT

english = int(input())
English = set(map(int, input().split()))
french = int(input())
French = set(map(int, input().split()))

print(len(English.union(French)))