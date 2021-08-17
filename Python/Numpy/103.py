import numpy as np



list1 = []
list2 = []

n, m, p = map(int, input().split())
for i in range(n):
    a = list(map(int,input().split()))
    list1.append(a)
    
for i in range(m):
    b = list(map(int, input().split()))
    list2.append(b)
    
arr1 = np.array(list1)
arr2 = np.array(list2)

print(np.concatenate((arr1, arr2),axis=0))