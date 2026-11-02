class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        best = 0
        pre = float("+inf")
        for n in prices:
            if n > pre:
                best = max(n - pre, best)
            else:
                pre = n
        return best
        