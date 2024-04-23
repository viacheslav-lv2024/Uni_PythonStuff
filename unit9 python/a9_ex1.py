import os
import re

def search_matches(filename: str, encodingtype: str, pattern: str) -> list:
    if encodingtype == "":
        encodingtype = "utf-8"
    if not (os.path.exists(filename) and os.path.isfile(filename)):
        raise ValueError(f"{filename} is not a file")
    with open(filename, "r", encoding=encodingtype) as file:
        fileContent = file.read()
        return re.findall(pattern, fileContent)
            

input_file = input("Enter file name: ")
input_encoding = input("Enter character encoding or press ENTER for default (utf-8): ")

input_pattern = input("Enter pattern or press ENTER to exit: ").strip()

while input_pattern:
    matches = search_matches(input_file, input_encoding, input_pattern)
    print(f"{input_pattern}: {matches}")
    input_pattern = input("Enter pattern or press ENTER to exit: ").strip()

