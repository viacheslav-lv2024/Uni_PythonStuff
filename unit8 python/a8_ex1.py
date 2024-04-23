import math

class Angle:
    def __init__(self, degree: float = None, radian: float = None):
        try:
            if radian is None and degree is None:
                print("Either degree or radian must be specified.")
                raise ValueError
            elif radian is None:
                self.radian = self.deg_to_rad(degree)
                self.degree = degree
            elif degree is None:
                self.degree = self.rad_to_deg(radian)
                self.radian = radian
            else:
                self.degree = degree
                self.radian = radian
                self.consistency()
        except ValueError as ex:
            raise ex
    def consistency(self):
        if not math.isclose(self.deg_to_rad(self.degree), self.radian):
            print("Degree and radian are not consistent.")
            raise ValueError
    def __eq__(self, other):
        if isinstance(other, Angle):
            if math.isclose(other.degree, self.degree) and math.isclose(other.radian, self.radian):
                return True
            else:
                return False
        else:
            return NotImplemented
    def __repr__(self):
        return f"Angle(degree={self.degree:.3f}, radian={self.radian:.3f})"
    def __str__(self):
        return f"{self.degree:.2f} deg = {self.radian:.2f} rad"
    def __add__(self, other):
        if isinstance(other, Angle):
            return Angle(degree=self.degree+other.degree, radian=self.radian+other.radian)
        else:
            return NotImplemented
    def __iadd__(self, other):
        if isinstance(other, Angle):
            self.degree += other.degree
            self.radian += other.radian
            self.consistency()
            return self
    @staticmethod
    def deg_to_rad(degree):
        return degree * (math.pi/180)
    @staticmethod
    def rad_to_deg(radian):
        return radian * (180/math.pi)
    @staticmethod
    def add_all(angle, *angles):
        sum = angle.degree
        for element in angles:
            sum += element.degree
        return Angle(degree=sum)
    
