class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = prices[0]
        max_profit = 0

        for price in prices:
            # Update max profit with selling today
            max_profit = max(max_profit, price - min_price)

            # Update minimum price seen so far
            min_price = min(min_price, price)

        return max_profit
                