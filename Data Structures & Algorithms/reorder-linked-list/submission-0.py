# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        h = head
        def get_last(head):
            t = None
            j = 0
            while head.next:
                j+=1
                # print("get_last", head.val, "next", head.next.val)
                t = head
                head = head.next
            t.next = None
            return head
        i = 0
        while head:
            # print("head in while", head.val)
            i += 1       
            if i %2 and head.next:
                temp = get_last(head)
                temp.next = head.next
                head.next = temp
                head = head.next


            else:
                head = head.next
        return head