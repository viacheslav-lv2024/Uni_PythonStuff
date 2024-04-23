def round_(number, ndigits: int = None):
    if ndigits is None:
        if number - int(number) >= 0.5:
            return int(number) + 1
        else:
            return int(number)
    int_part = int(number)
    decimal_part = ((number - int_part) * 10**ndigits)
    
    if decimal_part - int(decimal_part) >= 0.5:
        decimal_part = int(decimal_part) + 1
    else:
        decimal_part = int(decimal_part)
    
    decimal_part /= (10**ndigits)
    
    return int_part + decimal_part
    