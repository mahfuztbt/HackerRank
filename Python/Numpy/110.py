import numpy as np



n,m = map(int,input().split())
list1=[]
for i in range(n):
    l=list(map(int,input().split()))
    list1.append(l)
arr=np.array(list1)
np.set_printoptions(legacy='1.13')

print(np.mean(arr, axis=1))
print(np.var(arr, axis=0))

print(np.std(arr))
