input_file = input()
input_encoding = input()

input_pattern = " "

def search_matches(filename: str, pattern, encodingtype: str='utf-8'):
    if encodingtype == "":
        encodingtype = "utf-8"
    print(filename)
    print(pattern)
    print(encodingtype)
    
search_matches(input_file, input_pattern, input_encoding)