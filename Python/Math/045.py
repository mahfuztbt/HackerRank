# Enter your code here. Read input from STDIN. Print output to STDOUT
import cmath
c = complex(input().strip())
for i in cmath.polar(c):
    print(i)