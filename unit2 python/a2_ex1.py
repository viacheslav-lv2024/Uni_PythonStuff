n = int(input())
postal_code = 0
price_with_postal_code = 0
if n <= 0:
    print("Invalid subscription duration")
    exit(0)
elif n < 6:
    print("The price per month is 6.50")
    print(f"The full price for {n} months is {n * 6.50:.2f}")
elif n < 12:
    print("The price per month is 5.90")
    print(f"The full price for {n} months is {n * 5.90:.2f}")
else:
    postal_code = int(input("Please enter your postal code: "))
    if 1000 <= postal_code <= 9999:
        price_with_postal_code = 4 + (postal_code / 1000 - postal_code // 1000)
        print(f"The price per month is {price_with_postal_code:.2f}")
        print(f"The full price for {n} months is {price_with_postal_code * n:.2f}")
    else:
        print("Invalid postal code")

    
    