class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = float('inf')
        max_profit = 0

        for i in prices:
            if (i < min_price):
                min_price = i
            # max_profit = max(max_profit, price - min_price)  # Check profit
            if ((i - min_price) > max_profit):
                max_profit = i - min_price
        return max_profit
        