# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        i = 0
        t = head
        while t:
            t = t.next
            i += 1
        half = i//2 +1 if i %2 else i/2
        t = head
        i = 0
        end = None
        while i<half and t:
            end = t
            t = t.next
            i += 1
        
        end.next = None
        pre = None
        rev = None
        while t:
            rev = t
            t = t.next
            rev.next = pre
            pre = rev
        
        # while tmp:
            # print(tmp.val)
            # tmp = tmp.next


        s = head
        while head and rev:
            tmp = head.next

            head.next = rev
            head = head.next
            rev = rev.next
            head.next = tmp
            head = head.next
        # while s:
        #     print(s.val)
        #     s = s.next
        