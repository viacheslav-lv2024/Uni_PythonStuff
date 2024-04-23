from a7_ex3 import Distance
from a7_ex4 import Minkowski

class Euclidean(Minkowski):
    def __init__(self, x: int, vect1: list, vect2: list):
        self.euclidean_dist = 0
        self.number = x
        self.vect1 = vect1
        self.vect2 = vect2
    def to_string(self) -> str:
        return f"Euclidean: the number of vectors = {self.number}"
    def dist(self):
        for i in range(len(vect1)):
            self.euclidean_dist += (self.vect1[i] - self.vect2[i])**2
        self.euclidean_dist = self.euclidean_dist**0.5
        return float(f"{self.euclidean_dist:.4f}")

vect1 = [1,2,3]
vect2 = [4,5,6]
e = Euclidean(2, vect1, vect2)

