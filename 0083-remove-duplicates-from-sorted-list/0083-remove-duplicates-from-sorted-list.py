# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dum = head
        if not dum:
            return head
        while dum:
            if dum.next:
                if (dum.val == dum.next.val) and dum.next.next:
                    dum.next = dum.next.next
                    continue
                elif (dum.val == dum.next.val) and not dum.next.next:
                    dum.next = None
            dum = dum.next
            
        return head