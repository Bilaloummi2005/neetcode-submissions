class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        open = {
            "{":"}",
            "(":")",
            "[":"]"
        }
        close = {
            "}":"{",
            ")":"(",
            "]":"["
        }

        for c in s:
            if open.get(c):
                stack.append(c)
                continue
            if len(stack) == 0:
                return False
            o = stack.pop()
            if close.get(c) == o:
                continue
            return False
        if len(stack) == 0:
            return True
        return False