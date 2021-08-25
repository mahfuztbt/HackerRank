import numpy as np



n, m = map(int,input().split())
list1=[]
for i in range(n):
    l=list(map(int,input().split()))
    list1.append(l)
arr=np.array(list1)
print(np.max(np.min(arr,axis=1)))