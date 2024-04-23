class Radian:
    def __init__(self, degree: float):
        self.degree = degree
    def rad(self) -> float:
        self.rad = self.degree * (3.14/180.0)
        return f"{self.rad:.2f}"
    def print(self):
        print(f"The degree is {self.degree:.2f} and the radian is {self.rad:.2f}")


c = Radian(90)
print(c.rad())
c.print()