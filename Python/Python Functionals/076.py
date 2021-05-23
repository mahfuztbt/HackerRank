cube = lambda x: pow(x,3) #complete the lambda function 

def fibonacci(n):
    # return a list of fibonacci numbers
    list = [0,1]
    for i in range(2,n):
        list.append(list[i-2] + list[i-1])
    return(list[0:n])

if __name__ == '__main__':