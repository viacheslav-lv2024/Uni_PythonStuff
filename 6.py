day = int(input())
first_day_of_month_weekday = int(input())
answer = (day + first_day_of_month_weekday - 2) % 7 + 1
print(answer)