from typing import List

class MaxProfitSolution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        valley = prices[0]
        peak = prices[0]
        i = 0
        limit = len(prices) - 1

        while i < limit:
            # First find valley
            while i < limit and prices[i+1] <= prices[i]:
                i = i + 1
            valley = prices[i]

            # Next find the peak
            while i < limit and prices[i+1] >= prices[i]:
                i = i + 1
            peak = prices[i]

            max_profit = max_profit + (peak - valley)

        return max_profit
