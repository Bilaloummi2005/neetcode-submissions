class MyNode:
    def __init__(self, key, val, next=None, prev=None):
        self.key = key
        self.val = val
        self.next = next
        self.prev = prev


class LRUCache:

    def __init__(self, capacity: int):
        self.cash = {}
        self.most_used = MyNode(1000, 1000)
        self.most_used.prev = self.least_used = MyNode(0, 0, self.most_used)
        self.cap = capacity

    def get(self, key: int) -> int:
        if key in self.cash:
            node = self.cash.get(key)
            prev, nex = node.prev, node.next
            prev.next = nex
            nex.prev = prev
            prev, nex = self.most_used.prev, self.most_used
            prev.next = node
            node.prev = prev
            nex.prev = node
            node.next = nex
            return node.val
        return -1
        
        
    def add_node(self, key, value):
        if key in self.cash:
            self.delOne(self.cash[key])
        nex, prev = self.most_used, self.most_used.prev
        node = MyNode(key, value, nex, prev)
        nex.prev = node
        prev.next = node
        return node

    def delOne(self, todel=None):
        if todel:
            prev = todel.prev
        else:
            todel, prev = self.least_used.next, self.least_used
        key = todel.key
        prev.next = todel.next
        todel.next.prev = prev
        self.cash.pop(key)

    # def print_nodes(self):
    #     tmp = self.least_used
    #     while tmp:
    #         print(tmp.key, tmp.val, " | ", end="")
    #         tmp = tmp.next
    #     print()

    def put(self, key: int, value: int) -> None:
        self.cash[key] = self.add_node(key, value)
        if len(self.cash) > self.cap:
            self.delOne()


# time O(1) for put() and get()
# spcae O(n)

