import os
def print_directory_recursively(dir_path: str, level = 0):
    level += 1
    for dir_name in reversed(os.listdir(dir_path)):
        path = os.path.join(dir_path, dir_name)
        if os.path.isdir(path):
            print(level * "    ", dir_name, sep="")
            print_directory_recursively(path, level)
        elif os.path.isfile(path):
            print(level * "    ", dir_name, sep="")
            
print_directory_recursively("d0")