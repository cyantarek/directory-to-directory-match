import os

first_dir = os.listdir('.')
second_dir = os.listdir(r'second_dir_path')

for f in first_dir:
    if f in second_dir:
        pass
    else:
        print(f)
    
