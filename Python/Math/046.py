# Enter your code here. Read input from STDIN. Print output to STDOUT

import math

if __name__ == "__main__":
    x = int(input())
    y = int(input())
    
    print("{:}° ".format(int(round(math.degrees(math.atan2(x, y))))))