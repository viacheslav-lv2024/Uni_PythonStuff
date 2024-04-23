class Arr:
    def count(self, array):
        if len(array) == 0:
            return 0
        else:
            return 1 + self.count(array[1:])

input1 = Arr()
input2 = Arr()

print(input1.count([1, 2, 3, 4, 5]))
print(input2.count([15, 15, -10, 19, 17, 101, 203, -101]))

