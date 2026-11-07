class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        big = float("-inf")
        for i, h in enumerate(heights):
            m = h
            k = i
            if stack:
                while h < stack[-1][0]:
                    preh, j = stack.pop()
                    m = preh * (i-j)
                    k = j
                    big = max(big, m)
                    if not stack:
                        break
            
            stack.append((h, k))
            big = max(big, m)
        l = len(heights)
        for h, i in stack:
            big = max(big, (l-i)*h)
        

        return big

# time O(n)
# space O(n)

