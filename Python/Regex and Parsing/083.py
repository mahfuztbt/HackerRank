# Enter your code here. Read input from STDIN. Print output to STDOUT

import re
s = input()
k =input()

pattern = re.compile(k)
m = pattern.search(s)

if not m:
    print("(-1,-1)")
else:
    while m:
        print("({0}, {1})".format(m.start(),m.end()-1))
        m = pattern.search(s,m.start()+1)