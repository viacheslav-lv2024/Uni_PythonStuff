class ArrSum:
    def summ(self, array):
        if len(array) == 0:
            return None
        elif len(array) == 1:
            return array[0]
        else:
            return array[0] + self.summ(array[1:])

input1 = ArrSum()
input2 = ArrSum()

print(input1.summ([1, 2, 3, 4, 5]))
print(input2.summ([15, 15, -10]))