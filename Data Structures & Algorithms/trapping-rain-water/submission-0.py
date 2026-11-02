class Solution:
    def trap(self, height: [int]) -> int:
        suffex = [0 for _ in height]
        max_first = 0
        
        for i, n in enumerate(height):
            
            if max_first < n:
                h = 0
            else:
                h = max_first - n
            suffex[i] = h
            max_first = max(n, max_first)
        max_last = 0
        i = len(height) - 1
        while i > 0:
            n = height[i]
            if n < max_last:
                h = max_last - n
            else:
                h = 0
            suffex[i] = min(suffex[i], h)
            max_last = max(n, max_last)
            i-=1
        out = 0
        for n in suffex:
            out += n
        return (out)
    

