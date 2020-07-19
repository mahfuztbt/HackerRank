# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys

n = int(sys.stdin.readline().strip())

phone_book = dict()

for i in range(n):
    entry = sys.stdin.readline().strip().split(" ")
    phone_book[entry[0]] = entry[1]

query = sys.stdin.readline().strip()
while query:
    phone_number = phone_book.get(query)
    if phone_number:
        print(query + "=" + phone_number)
    else:
        print("Not found")
    query = sys.stdin.readline().strip()