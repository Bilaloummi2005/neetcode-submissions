# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow, fast = head, head
        while fast:
            slow = slow.next
            if fast.next and fast.next.next:
                fast = fast.next.next
            else:
                return False
            if slow is fast:
                return True
        return False
    
# time O(n)
# space O(1)