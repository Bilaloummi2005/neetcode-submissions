# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode()
        h = head
        while list1 or list2:
            if list1 and not list2:
                head.next = list1
                break
            elif list2 and not list1:
                head.next = list2
                break
            if list1 and list1.val <= list2.val:
                head.next = list1
                head = head.next
                list1 = list1.next
            elif list2 and list2.val < list1.val:
                head.next = list2
                head = head.next
                list2 = list2.next
        return h.next

    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if lists == []:
            return 
        l = len(lists)
        i = 0
        out = lists
        while len(out)>1:
            lists = out
            out = []
            i = 0
            while i < len(lists):
                f = lists[i]
                i += 1
                if i >= len(lists):
                    out.append(f)
                    break
                s = lists[i]
                i+=1
                out.append(self.mergeTwoLists(f, s))
        return out[0]



















