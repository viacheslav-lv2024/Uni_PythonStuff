def print_directory(dir_path: str):
    import os
    if not (os.path.isfile(dir_path) or os.path.isdir(dir_path)):
        print(f"{dir_path} is invalid")
        return
    if os.path.isfile(dir_path):
        print(f"{dir_path} is a file not a directory")
        return
    def print_directory_recursively(dir_path: str, level):
        level += 1
        for dir_name in reversed(os.listdir(dir_path)):
            path = os.path.join(dir_path, dir_name)
            if os.path.isdir(path):
                print((level + 1) * "    ", dir_name, sep="")
                print_directory_recursively(path, level)
            elif os.path.isfile(path):
                print((level + 1) * "    ", dir_name, sep="")
    level = 0
    print(f"path_to_the_directory_{dir_path}")
    for dir_name in reversed(os.listdir(dir_path)):
        path = os.path.join(dir_path, dir_name)
        if os.path.isdir(path):
            print("    ", dir_name, sep="")
            print_directory_recursively(path, level)
        elif os.path.isfile(path):
            print("    ", dir_name, sep="")

