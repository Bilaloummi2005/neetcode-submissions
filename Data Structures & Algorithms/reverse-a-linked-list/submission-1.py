# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp = None
        while head:
            t = head
            head = head.next
            t.next = temp
            temp = t
        return temp

# time O(n)
# space O(1)