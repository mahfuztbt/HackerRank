import numpy



n,m = map(int,input().split())
array = numpy.array([input().split() for i in range(n)], int)

print(numpy.prod(numpy.sum(array,axis=0)))