import os
print("Test a path exists or not:")
path = "C:\\Users\\PC\\Desktop\\Python\\git\\notes.txt"
print(os.path.exists(path))
if(os.path.exists(path)):
    print(os.path.split(path))
    print("\nfilename:")
    print(os.path.basename(path))

    print("\ndirname:")
    print(os.path.dirname(path))