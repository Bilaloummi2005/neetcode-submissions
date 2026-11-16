class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        if len(tokens) == 1:
            return int(tokens[0])
        ops = {
            "+": lambda a, b: a+b,
            "-": lambda a, b: a-b,
            "*": lambda a, b: a*b,
            "/": lambda a, b: a/b
        }
        stack = []
        for e in tokens:
            if not e in ops:
                stack.append(int(e))
                continue
            op = ops[e]
            e1 = stack.pop()
            e2 = stack.pop()
            res = int(op(e2, e1))
            stack.append(res)

        return (res)