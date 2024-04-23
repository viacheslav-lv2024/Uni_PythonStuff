class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
l1 = []

for i in range(3):
    l1.append(ListNode(i))
for i in range(3):
    print(l1[i])

print(l1)