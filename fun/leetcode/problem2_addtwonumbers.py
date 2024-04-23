# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        size = 0
        num = l1.val
        while num:
            size += 1
            num = l1.next
        def calculate_number(linked_list, list_size):
            number = 0
            element = linked_list.val
            for i in range(list_size):
                number += element * 10**i
                element = linked_list.next
            return number
        first_number = calculate_number(l1, size)
        second_number = calculate_number(l2, size)
        summ = first_number + second_number
        summ = str(summ)
        summ = summ[::-1]
        l3 = ListNode()
        l3.val = int(summ[-1])
        for i in range(size-2, 1, -1):
            l3.next = int(sum[i])
            
        number = l3.val
        for i in range(size-1, 1, -1):
            print(number)
            number = l3.next
        
l1 = ListNode()
l2 = ListNode()

l1.val = 2
l1.next = 4
l1.next = 3
l1.next = None

l2.val = 5
l2.next = 6
l2.next = 4
l2.next = None

answer = Solution()
answer.addTwoNumbers(l1, l2)