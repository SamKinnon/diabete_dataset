import os
directory = "C:/Users/pc/Downloads"
files = [f for f in os.listdir(directory) if f.endswith('.xlsx')]
print(files)
