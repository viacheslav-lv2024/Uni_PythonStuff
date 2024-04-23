import os

def file_statistics(path: str):
    try:
        if os.path.exists(path):
            if os.path.splitext(path)[1] != ".txt":
                raise ValueError
        if not os.path.exists(path):
            raise OSError
        with open(path, encoding="utf-8") as f:
            cnt_l = 0
            for _ in f:
                cnt_l += 1
        with open(path, encoding="utf-8") as f:
            cnt_w = 0
            for line in f.readlines():
                for word in line.split():
                    cnt_w += 1
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
    except ValueError:
        print(f"ValueError: Path {path} is not a text file")
    except OSError:
        print(f"OSError: Path {path} does not exist")
