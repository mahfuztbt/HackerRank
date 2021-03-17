# Enter your code here. Read input from STDIN. Print output to STDOUT

n1, n2 = (int(input()) for i in range(2))
num = divmod(n1, n2)
print(num[0])
print(num[1])
print(num)