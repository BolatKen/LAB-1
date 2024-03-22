import re

f = open(r"C:\Users\PC\Desktop\Python\lab1\LAB5\row.txt", encoding = 'utf-8')
s = str(f.read())

x = re.search("a.*b$", s)

if x:
    print("Yes")
else:
    print("No")