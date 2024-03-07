import os
print("Test a path exists or not:")
path = "C:\\Users\\PC\\Desktop\\Python\\git\\notes.txt"
print(os.path.exists(path))
path = "C:\\Users\\PC\\Desktop\\Python\\git\\notes.txt"
print("\nFile name of the path:")
print(os.path.basename(path))
print("\nDir name of the path:")
print(os.path.dirname(path))