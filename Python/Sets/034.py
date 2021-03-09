# Enter your code here. Read input from STDIN. Print output to STDOUT
l=[]
english = int(input())
English = set(map(int,input().split()))

french = int(input())
French = set(map(int,input().split()))

inter = English.intersection(French)

print(len(inter))