class Solution:
    def replaceElements(self, arr: list[int]) -> list[int]:
        # first max = -1
        # reverse iteration
        # compare known maximum with the new number with each iteration
        right_maximum = -1
        for i in range(len(arr)-1, -1, -1):
            new_maximum = max(right_maximum, arr[i])
            arr[i] = right_maximum
            right_maximum = new_maximum
        return arr

a = Solution()

print(a.replaceElements([17,18,5,4,6,1]))