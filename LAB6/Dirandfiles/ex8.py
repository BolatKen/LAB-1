import os
path = "C:\\Users\\PC\\Desktop\\muhammad-yunnus.jpg"
if os.path.exists(path):
  os.remove(path)
else:
  print("The file does not exist")