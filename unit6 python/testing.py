def file_statistics(path: str):
    try:
        with open(path, encoding="utf-8") as f:
            cnt_l = sum(1 for _ in f)
        
        with open(path, encoding="utf-8") as f:
            cnt_w = sum(len(line.split()) for line in f.readlines())
        
        with open(path, encoding="utf-8") as f:
            cnt_char = 0
            cnt_digits = 0
            lines = f.read()
            for element in lines:
                cnt_char += 1
                if element.isdigit():
                    cnt_digits += 1

        print(f"""Number of lines: {cnt_l}
Number of words: {cnt_w}
Number of characters: {cnt_char}
Number of digits: {cnt_digits}""")
    
    except FileNotFoundError:
        raise OSError(f"Incorrect path: {path}")
    
    except UnicodeDecodeError:
        raise ValueError(f"Wrong file type or encoding: {path}")

# Example Usage:
try:
    file_statistics('Examples/ex1_1.txt')
    file_statistics('nonexistent_file.txt')  # Raises OSError
    file_statistics('Examples/ex1_4.py')  # Raises ValueError
except (OSError, ValueError) as e:
    print(e)
