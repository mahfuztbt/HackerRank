import numpy

def arrays(arr):
    # complete this function
    # use numpy.array
    arr1 = arr[::-1]
    numpy_array = numpy.array(arr1, float)
    return numpy_array

arr = input().strip().split(' ')
result = arrays(arr)
print(result)