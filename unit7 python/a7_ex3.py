class Distance:
    def __init__(self, x: int):
        self.number = x
    def to_string(self) -> str:
        return f"Distance: the number of vectors = {self.number}"
    def dist(self) -> float:
        raise NotImplementedError
    
vect1 = [1,2,3]
vect2 = [4,5,6]
d = Distance(2)


