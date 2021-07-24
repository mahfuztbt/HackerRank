# Enter your code here. Read input from STDIN. Print output to STDOUT

import re

for i in range(int(input())):
    print(re.sub(r'(?<= )\|\|(?= )', 'or', re.sub(r'(?<= )&&(?= )','and',input())))