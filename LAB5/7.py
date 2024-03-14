import re

f = open("row.txt", encoding = 'utf-8')
s = str(f.read())

x = re.split("[A-Z]", s)

print(x)
