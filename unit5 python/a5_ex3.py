def gen_fibonacci(upper_bound):
    if not (type(upper_bound) == float or type(upper_bound) == int):
        raise TypeError
    if upper_bound < 0:
        raise ValueError
    x, y = 0, 1
    while x <= upper_bound:
        yield x
        x, y = y, x+y
