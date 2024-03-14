import re

f = open("row.txt", encoding = 'utf-8')
s = str(f.read())

x = re.sub('(?!^)(?=[A-Z])', ' ', s)

print(x)