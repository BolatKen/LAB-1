f = open(r"C:\Users\PC\Desktop\Python\lab1\LAB6\Dirandfiles\text.txt", "r")
l = open("text2.txt", "a")
for x in f:
    l.write(x)
