number = int(input())
answer = number // 1000 + (number // 100) % 10 + (number // 10) % 10 + number % 10
print(answer)