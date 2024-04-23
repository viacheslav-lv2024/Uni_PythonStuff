class Power:
    def __init__(self, exponent: float):
        if not (isinstance(exponent, (int, float))):
            raise TypeError("The exponent must be a numerical value.")
        self.exponent = exponent
    def __call__(self, x):
        if not isinstance(x, (int, float)):
            raise TypeError("Input must be a numerical value.")
        return x**self.exponent
    def __mul__(self, other):
        if isinstance(other, (int, float)):
            new_exponent = self.exponent + other
            return Power(new_exponent)
        elif isinstance(other, Power):
            return Power(self.exponent+other.exponent)
        else:
            return NotImplemented

class Square(Power):
    def __init__(self, x=None):
        self.exponent = 2
        if x:
            super().__call__(x)


