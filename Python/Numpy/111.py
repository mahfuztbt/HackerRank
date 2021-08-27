import numpy



n=int(input())
a = numpy.array([input().split() for i in range(n)], int)
b = numpy.array([input().split() for i in range(n)], int)
m = numpy.dot(a,b)

print(m)