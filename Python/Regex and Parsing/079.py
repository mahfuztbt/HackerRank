# Enter your code here. Read input from STDIN. Print output to STDOUT

import re

class DetectFloat():
    def __init__(self):
        self.n = int(input())
        
        for i in range(self.n):
            self.s =  input()
            regex = "^[-+]?[0-9]*\.[0-9]+$"
            print(bool(re.match(regex,self.s)))
            
if __name__ == "__main__":
    object0=DetectFloat()