f = open("text.txt", "r")
l = open("text2.txt", "a")
DataToCopy = ""
for x in f:
    l.write(x)
