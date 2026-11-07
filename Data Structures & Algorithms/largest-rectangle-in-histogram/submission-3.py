class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        big = float("-inf")
        for i, h in enumerate(heights):
            k = i
            while stack and h < stack[-1][0]:
                preh, j = stack.pop()
                m = preh * (i-j)
                k = j
                big = max(big, m)
        
            stack.append((h, k))
        l = len(heights)
        for h, i in stack:
            big = max(big, (l-i)*h)
        

        return big

# time O(n)
# space O(n)

