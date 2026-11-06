class MinStack:

    def __init__(self):
        self.stack = []
        self.mininimal = float("+inf")
        

    def push(self, val: int) -> None:
        if type(val) is int:
            self.mininimal = min(self.stack[-1][1] if len(self.stack) else float("inf"), val)
            self.stack.append((val, self.mininimal))
        else:
            self.stack.append(null)

    def pop(self) -> None:
        
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1][0]
        

    def getMin(self) -> int:
        return self.stack[-1][1]      

# [null,null,null,null,-3,null,0,-2,null,null,null,-4,null,-4,null,2,-3,null,0,-2]
# [null,null,null,null,-3,null,0,-2,null,null,null,-4,null,-4,null,2,-2,null,0,-2]
