from a7_ex3 import Distance

class Minkowski(Distance):
    def __init__(self, x: int, vect1: list, vect2: list):
        self.minkowski_dist = 0
        self.number = x
        self.vect1 = vect1
        self.vect2 = vect2
    def to_string(self) -> str:
        return f"Minkowski: the number of vectors = {self.number}"
    def dist(self):
        for i in range(len(vect1)):
            self.minkowski_dist += (self.vect1[i] - self.vect2[i])**self.number
        self.minkowski_dist = self.minkowski_dist**(1/self.number)
        return float(f"{self.minkowski_dist:.4f}")
    
vect1 = [1,2,3]
vect2 = [4,5,6]
k = Minkowski(2, vect1, vect2)

