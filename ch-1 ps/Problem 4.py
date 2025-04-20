# write an python program to print the contents of a directory using the os module. search online for the function which does that  

import os

# Specify the directory path
path = '.'  # Current directory

try:
    # Get the list of all files and directories
    dir_list = os.listdir(path)
    print(f"Contents of '{path}':")
    for item in dir_list:
        print(item)
except FileNotFoundError:
    print(f"The directory '{path}' does not exist.")
except PermissionError:
    print(f"Permission denied to access '{path}'.")
