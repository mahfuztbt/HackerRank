# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
for i in range(n):
    data = input().rstrip()
    even = []
    odd = []

    i = 0
    while(i<len(data)):
        even.append(data[i])
        i+=1
        if i < len(data):
            odd.append(data[i])
            i += 1

    even = ''.join(even)
    odd = ''.join(odd)

    print(even, odd)