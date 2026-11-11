import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        piles = sorted(piles)
        r = piles[-1]
        l = 1
        best = 0
        while l <= r:
            mid = (r + l)//2
            dev = 0
            for b in piles:
                dev += math.ceil(b/mid)
            if dev <= h:
                best = mid
                r = mid -1
            else:
                l = mid + 1
            # print(best, dev)
        return best









