def f(x: int):
    try:
        g(x)
        print("f1")
    except ValueError:
        print("f2")
    finally:
        print("f3")

def g(x: int):
    try:
        h(x)
        print("g1")
    except ValueError:
        print("g2")
    except TypeError:
        print("g3")
    if x < -10:
        raise NameError
        print("g4")
    else:
        print("g5")
    print("g6")

def h(x: int):
    try:
        if x > 10:
            raise ValueError
        if x < 0:
            raise TypeError
    finally:
        print("h1")
    print("h2")
    
f(-11)
