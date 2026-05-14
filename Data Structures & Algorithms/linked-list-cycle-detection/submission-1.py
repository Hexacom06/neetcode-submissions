# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head:
            s, f = head, head.next
        else:
            return False
        while f and f.next:
            if s == f: return True
            s, f = s.next, f.next.next 
        return False