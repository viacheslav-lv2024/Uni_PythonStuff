time = int(input())
hours = time // 3600
minutes = (time - hours * 3600) // 60
print('It is', hours, 'hours', minutes, 'minutes.')