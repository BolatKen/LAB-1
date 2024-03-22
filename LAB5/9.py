import re

def snake(s):
    return re.sub("(?!^)(?=[A-Z])", '_', s).lower()

f = open(r"C:\Users\PC\Desktop\Python\lab1\LAB5\row.txt", encoding='utf-8')
s = input()
ans = snake(s)

print(ans)