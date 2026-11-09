class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        best = 0
        for r in range(len(prices)):
            n = prices[r]
            while prices[l] > n:
                l += 1
                best = max(best, n - prices[l])
            best = max(best, n - prices[l])
            
        return best
        