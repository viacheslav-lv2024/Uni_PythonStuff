start = int(input("Start: "))
stop = int(input("Stop: "))
step = int(input("Step: "))
even_number_cnt = 0
odd_number_sum = 0
cnt = 0
if (stop - start) > step:
    for i in range(start, stop, step):
        if cnt <= 4:
            print(f"Number in iteration {cnt} = {i}")
        cnt += 1
        if i % 2 == 0:
            even_number_cnt += 1
        else:
            odd_number_sum += i
print(f"Even number count = {even_number_cnt}")
print(f"Sum of odd numbers = {odd_number_sum}")
