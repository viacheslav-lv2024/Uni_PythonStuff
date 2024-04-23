degree = int(input())
hours = degree // 30
minutes = (degree - hours * 30) * 2
print('It is', hours, 'hours', minutes, 'minutes.')