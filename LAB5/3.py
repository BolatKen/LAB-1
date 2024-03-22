import re

f = open(r"C:\Users\PC\Desktop\Python\lab1\LAB5\row.txt", encoding = 'utf-8')
s = input()

x = re.search("[a-z]+_[a-z]+", s)

if x:
    print("There is a match")
else:
    print("There is no match")