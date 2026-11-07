class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        i = len(temperatures) - 1
        out = [0 for _ in temperatures]
        while i >= 0:
            t = temperatures[i]
            while stack and t >= stack[-1][0]:
                stack.pop()

            out[i] = stack[-1][1] - i if stack else 0
            stack.append((t, i))
            i-=1
        return out
