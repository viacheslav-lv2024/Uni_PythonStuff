print("""==================================================
PC Parts Store - Order
==================================================""")
cables_number = int(input("Number of cables: "))
monitors_number = int(input("Number of monitors: "))
keyboards_number = int(input("Number of keyboards: "))
print(f"""{cables_number:>3} cables (9.90 EUR each) = {cables_number * 9.9:.2f} EUR
{monitors_number:>3} monitors (249.99 EUR each) = {monitors_number * 249.99:.2f} EUR
{keyboards_number:>3} keyboards (27.50 EUR each) = {keyboards_number * 27.5:.2f} EUR
--------------------------------------------------
Total: {cables_number * 9.9 + monitors_number * 249.99 + keyboards_number * 27.5:.2f} EUR
==================================================""")
