day_number, lesson_number = list(map(int, input().split()))
answer = (day_number - 1) * 6 + lesson_number
print(answer)