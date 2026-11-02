class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_area = 0
        first = 0
        last = len(heights) - 1
        while first < last:
            min_height = min(heights[first], heights[last])
            width = last - first
            max_area = max(max_area, min_height * width)
            if heights[first] > heights[last]:
                last -= 1
            else:
                first += 1
        return max_area