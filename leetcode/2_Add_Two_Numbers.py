# Medium
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        result = curr = ListNode(0)
        p1 = l1
        p2 = l2
        carry = 0
        while p1 != None or p2 != None:
            x = p1.val if p1 != None else 0
            y = p2.val if p2 != None else 0
            currSum = carry + x + y
            carry = currSum // 10 if currSum // 10 != 0 else 0
            curr.next = ListNode(currSum%10)
            curr = curr.next
            p1 = p1.next if p1 != None else None
            p2 = p2.next if p2 != None else None
        if carry != 0:
            curr.next = ListNode(carry)
            
        return result.next