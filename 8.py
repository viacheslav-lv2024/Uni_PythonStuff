number = input()
length_of_number = len(number)
integer_part = number[:(length_of_number - 3)]
fractional_part = number[(length_of_number - 2):]
print(integer_part, fractional_part)