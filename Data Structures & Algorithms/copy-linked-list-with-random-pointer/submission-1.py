"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        copy = {}
        h = None
        while head:
            copy[head] = Node(head.val)
            if not h:
                h = copy[head]
            head = head.next

        for og, cp in copy.items():
            if og.next:
                cp.next = copy[og.next]
            if og.random:
                cp.random = copy[og.random]
        return h



# time O(n)
# space O(n)