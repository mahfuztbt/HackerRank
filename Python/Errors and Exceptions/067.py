# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
for i in range(int(input())):
    try:
        if re.findall(input(), "") != None:
            print(True)
    except re.error:
        print(False)