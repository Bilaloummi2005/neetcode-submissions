class MinStack:

    def __init__(self):
        self.stack = []
        self.min_el = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.min_el or val <= self.min_el[-1]:
            self.min_el.append(val)

    def pop(self) -> None:
        el = self.stack.pop()
        if self.min_el and el == self.min_el[-1]:
            self.min_el.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_el[-1]
