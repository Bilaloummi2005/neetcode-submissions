class Solution:
    def maxArea(self, heights: List[int]) -> int:
        best = 0
        l = 0
        r = len(heights) - 1
        while l < r:
            right = heights[r]
            left = heights[l]
            best = max(best, (r - l)*min(right, left))
            if right > left:
                l += 1
            else:
                r -= 1

        return best