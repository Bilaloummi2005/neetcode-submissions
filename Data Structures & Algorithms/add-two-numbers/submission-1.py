# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        pre = ListNode(0)
        head = pre
        i = 0
        n = 0
        while (l1 or l2) or n:
            if (l1 and l2):
                m = l1.val + l2.val + n
            elif l1:
                m = l1.val + n
            elif l2:
                m = l2.val + n
            else:
                m = n
            
            
            curr = ListNode(m%10)
            pre.next = curr
            pre = curr
            n = m //10
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
            i+=1
        return head.next

# time O(max(n, m))
# space O(1)

        