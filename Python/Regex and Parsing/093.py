# Enter your code here. Read input from STDIN. Print output to STDOUT

import re
t = re.compile(
    r"^"
    r"(?!.*(\d)(-?\1){3})"
    r"[456]"
    r"\d{3}"
    r"(?:-?\d{4}){3}"
    r"$"
)

for i in range(int(input().strip())):
    print("Valid" if t.search(input().strip()) else "Invalid")
