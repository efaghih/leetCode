class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        r = 1
        maxx = 0
        while r < len(prices):
            
            
            if (prices[r]-prices[l] < 0):
                l += 1
                r = l
            
            maxx = max(maxx, prices[r] - prices[l])

            r += 1
            
        return maxx
                