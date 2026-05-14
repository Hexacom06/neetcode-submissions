# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next: return
        s, f = head, head
        while f and f.next:
            f = f.next.next
            s = s.next
        curr = s.next
        s.next = None
        prev = None
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        forward, reverse = head, prev
        while reverse:
            temp = reverse.next
            reverse.next = forward.next
            forward.next = reverse
            reverse = temp
            forward = forward.next.next
        
