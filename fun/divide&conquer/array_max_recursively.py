class Arr:
    def find_max(self, array):
        if len(array) == 0:
            return None
        elif len(array) == 1:
            return array[0]
        else:
            if array[0] >= self.find_max(array[1:]):
                return array[0]
            else:
                return self.find_max(array[1:])

input1 = Arr()
input2 = Arr()

print(input1.find_max([1, 2, 3, 4, 5]))
print(input2.find_max([15, 15, -10, 19, 17, 101, 203, -101]))
