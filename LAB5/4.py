import re

f = open("row.txt", encoding = 'utf-8')
s = str(f.read())

x = re.search("[A-Z]+[a-z]+", s)

if x:
    print("Yes")
else:
    print("No")