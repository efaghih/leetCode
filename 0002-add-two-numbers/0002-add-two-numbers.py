# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        sum = dummy
        sum1 = 0
        sum2 = 0
        p = 1
        
        while l1 or l2:
            if l2 and l1:
                sum1 += (l1.val *  p) + (l2.val * p)
                l1 = l1.next
                l2 = l2.next
            elif l2:
                sum1 += (l2.val * p)
                l2 = l2.next
            elif l1:
                sum1 += (l1.val *  p)
                l1 = l1.next

            p *= 10
            
        
        print (sum1)
        sum1 = str(sum1)
        for i in range (len(sum1) - 1, -1, -1):
            sum.next = ListNode(int(sum1[i]))
            sum = sum.next
        return dummy.next 
        