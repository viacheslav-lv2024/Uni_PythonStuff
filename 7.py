rub, kop, n = map(int, input().split())
excessive_rub = (kop * n) // 100
total_kop = kop * n - excessive_rub * 100
total_rub = rub * n + excessive_rub
print(total_rub, total_kop)
