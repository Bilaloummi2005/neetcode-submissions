class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        if len(tokens) == 1:
            return int(tokens[0])
        stack = []
        op = {
            "+": lambda x,y: x+y,
            "-": lambda x,y: x-y,
            "*": lambda x,y: x*y,
            "/": lambda x,y: x/y
        }
        for i, n in enumerate(tokens):
            if n in op:
                f = stack.pop()
                l = stack.pop()
                res = int(op.get(n)(l, f))
                stack.append(res)
                continue
            stack.append(int(n))
        return res
        