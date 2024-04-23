def file_statistics(path: str):
    with open(path, newline="") as f:
        fc = f.read()

print(file_statistics("Examples/ex1_2.txt"))