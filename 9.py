hours1, minutes1, seconds1 = map(int, input().split())
hours2, minutes2, seconds2 = map(int, input().split())

ans = 3600 * (hours2 - hours1) + 60 * (minutes2 - minutes1) + (seconds2 - seconds1)
print(ans)