import numpy



if __name__ == "__main__":
    n, m = list(map(int, input().split()))
    lis = []
    
    for i in range(n):
        lis.append(list(map(int, input().split())))
        
    print(numpy.transpose(lis))
    print(numpy.array(lis).flatten())