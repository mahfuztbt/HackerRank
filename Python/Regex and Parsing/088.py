# Enter your code here. Read input from STDIN. Print output to STDOUT

import re

n = int(input())

for i in range(0,n):
    s = input()
    
    x = s.split()
    
    if len(x)>1 and "{" not in x:
        x = re.findall(r"#[a-fA-F0-9]{3,6}",s)
        [print(i) for i in x]