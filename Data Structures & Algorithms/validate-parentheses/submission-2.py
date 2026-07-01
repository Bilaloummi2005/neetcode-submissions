class Solution:
    def isValid(self, s: str) -> bool:
        opened = {"{": "}", "[": "]", "(":")"}
        closed = {"}": "{", "]": "[",")": "("}
        stack = []
        symb = ""
        try:
            for c in s:
                if opened.get(c):
                    stack.append(c)
                elif closed.get(c):
                    if  stack[-1] == closed.get(c):
                        stack.pop()
                    else:
                        return False
            return len(stack) == 0
        except Exception as e:
            return False