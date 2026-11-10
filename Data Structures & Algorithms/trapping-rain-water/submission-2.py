class Solution:
    def trap(self, height: List[int]) -> int:
        pref = [0]*len(height)
        d = 0
        for i, n in enumerate(height):
            pref[i] = max(d - n, 0)
            d = max(d, n)
        suf = [0]*len(height)
        i = len(height) - 1
        d = 0
        while i >= 0:
            suf[i] = min(max(d - height[i], 0), pref[i])
            d = max(d, height[i])
            i-=1
        return (sum(suf))