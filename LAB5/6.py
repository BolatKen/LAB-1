import re

f = open("row.txt", encoding = 'utf-8')
s = str(f.read())

patt = "[ .,]"

x = re.sub(patt, ':', s)

print(x)