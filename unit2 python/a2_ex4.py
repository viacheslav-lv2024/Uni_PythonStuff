lines = int(input())
if lines >= 3:
    for i in range(lines):
        if i == 0 or i == (lines - 1):
            print("-" * lines)
        else:
            print("|" + " " * (lines - 2) + "|")
else:
    print("Invalid number of lines")
