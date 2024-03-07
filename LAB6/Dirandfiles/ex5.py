color = ["colum", "word", "number"]
with open('s.txt', "w") as fr:
        for i in color:
                fr.write(i + '\n')
content = open('s.txt')
print(content.read())