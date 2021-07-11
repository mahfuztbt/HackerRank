# Enter your code here. Read input from STDIN. Print output to STDOUT

import re

s = input()
pattern = r'([a-z A-Z 0-9])\1'
m = re.search(pattern, s)

if m:
    print(m.groups()[0])
else:
    print(-1)