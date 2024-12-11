# Task 1: Directory Inspector:

# Problem Statement: Create a Python script that lists all files and subdirectories in a given directory. Your script should prompt the user for the directory path and 
# hen display the contents.

# Code Example:
#     import os

#     def list_directory_contents(path):
#         # List and print all files and subdirectories in the given path
# Expected Outcome: The script should correctly list all files and subdirectories in the specified directory. Handle exceptions for invalid paths or inaccessible directories.



import os
path = input("What directory would you like the contents of? ")  

def list_directory_contents(path= '.'):
    try:
        for entry in os.listdir(path):
            full_path = os.path.join(path, entry)
            if os.path.isdir(full_path):
                list_directory_contents(full_path)
            else:
                print(full_path)
    
    except FileNotFoundError:
        print("This directory does not exist.")
    except PermissionError:
        print("You do not have permission to view this directory.")

directory_path = './'    
list_directory_contents(directory_path)