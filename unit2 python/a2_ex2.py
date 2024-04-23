user_input = input("Enter number or 'x': ")
num_check = user_input
cnt = 0
while user_input != "x" and (int(user_input) % 10 == int(num_check) % 10):
    num_check = user_input
    user_input = input("Enter number or 'x': ")
    cnt += 1
if user_input == "x":
    if cnt == 0:
        print("Empty sequence")
    else:
        print("All numbers had the same digit in the ones place")
else:
    print(f"{num_check} and {user_input} differ in the ones place")


