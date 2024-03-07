def file(name):
    with open(name, "r") as f:
        counter = 0
        for x in f:
            counter += 1
    return counter


print("Number of lines in the file: ", file("text.txt"))