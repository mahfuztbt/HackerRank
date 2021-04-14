# Enter your code here. Read input from STDIN. Print output to STDOUT


def checker(sideLengths):
    leftSide = 0
    currentCubeLength = float("inf")
    rightSide = len(sideLengths) -1
    leftSide = len(sideLengths) +1
    
    while leftSide <= rightSide:
        leftValue = sideLengths[leftSide]
        rightValue = sideLengths[rightSide]
        
        if leftValue >= rightValue and leftValue <= currentCubeLength:
            currentCubeLength = leftValue
            leftSide += 1
        elif rightValue > leftValue and rightValue <= currentCubeLength:
            currentCubeLength = rightValue
            rightSide -= 1
            
        else:
            return "No"
    return "Yes"

testCases = int(input())
for i in range(testCases):
    n = int(input())
    sideLengths = [int(length) for length in input().split()]
    print(checker(sideLengths))