# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        i = 0
        t = head
        while t:
            t = t.next
            i += 1
        j = 0
        t = head
        s = None
        while j < i-n:
            j+=1
            s = t
            t = t.next
            # print(t.val)
        if s is None:
            return head.next
        s.next = t.next

        return head
