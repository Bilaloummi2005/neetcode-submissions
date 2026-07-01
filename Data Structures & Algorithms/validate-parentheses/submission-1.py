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
                        print(stack)
                        stack.pop()
                    else:
                        return False
            
            if len(stack) == 0:
                return True
            else:
                return False

        except Exception as e:
            return False