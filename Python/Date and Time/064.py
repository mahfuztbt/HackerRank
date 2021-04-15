# Enter your code here. Read input from STDIN. Print output to STDOUT
import calendar
 
weekday = ['MONDAY', 'TUESDAY', 'WEDNESDAY', 'THURSDAY','FRIDAY','SATURDAY','SUNDAY']

m,d,y = map(int,input().split())
A = calendar.weekday(y,m,d)

print(weekday[A])