import re

f = open("row.txt", encoding = 'utf-8')
s = str(f.read())

x = re.search("[a-z]+_[a-z]+", s)

if x:
    print("There is a match")
else:
    print("There is no match")