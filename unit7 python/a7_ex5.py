from a7_ex3 import Distance
import math

class Manhattan(Distance):
    def __init__(self, x: int, vect1: list, vect2: list):
        self.manhattan_dist = 0
        self.number = x
        self.vect1 = vect1
        self.vect2 = vect2
    def to_string(self) -> str:
        return f"Manhattan: the number of vectors = {self.number}"
    def dist(self):
        for i in range(len(vect1)):
            self.manhattan_dist += abs(self.vect1[i] - self.vect2[i])
        self.manhattan_dist = float(self.manhattan_dist)
        return f"{self.manhattan_dist:.4f}"

vect1 = [1,2,3]
vect2 = [4,5,6]    
m = Manhattan(2, vect1, vect2)

    
