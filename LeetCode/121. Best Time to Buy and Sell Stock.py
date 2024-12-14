from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Initialize variables for the minimum price and maximum profit
        min_price = float("inf")
        max_profit = 0

        for p in prices:
            if p < min_price:  # if current price in lower than min
                min_price = p  # use current price as new min

            profit = p - min_price  # calc profit

            if profit > max_profit:  # if current profit higher than max_profit
                max_profit = profit  # use current profit as max_profit
        return max_profit


prices = [[7, 1, 5, 3, 6, 4], [7, 6, 4, 3, 1]]
for i in prices:
    print(Solution().maxProfit(i))
