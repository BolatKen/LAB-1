import re

f = open(r"C:\Users\PC\Desktop\Python\lab1\LAB5\row.txt", encoding = 'utf-8')
s = input()

patt = "[ .,]"

x = re.sub(patt, ':', s)

print(x)