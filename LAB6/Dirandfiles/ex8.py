import os
path = r"C:\Users\PC\Desktop\Python\lab1\LAB6\text2.txt"
if os.path.exists(path):
  os.remove(path)
else:
  print("The file does not exist")