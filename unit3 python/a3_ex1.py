main_list = []
n_list = []
rows = int(input('Number of rows: '))
cols = int(input('Number of cols: '))

for i in range(rows):
    for j in range(cols):
        if j == i:
            n_list.append(1)
        else:
            n_list.append(0)
    main_list.append(n_list)
    n_list = []

print('  ', end='')
for k in range(cols):
    print(' ', k, sep='', end='')

print()
print('  ', end='')

for k in range(cols * 2 - 1):
    print('-', end = '')
print('-')  # last '-' must have '\n' following after

for i in range(rows):
    print(i, '|', sep='', end='')
    for j in range(cols):
        print(' ', main_list[i][j], end='', sep='')
    if i != rows - 1:
        print()