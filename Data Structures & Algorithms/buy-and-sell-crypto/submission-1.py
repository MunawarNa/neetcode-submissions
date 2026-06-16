class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        max_profit = 0
        start = 0
        end = 0

        while end < len(prices) :

            if prices[start] < prices[end]:
                max_profit = max(max_profit, prices[end] - prices[start])
            else:
                start = end
            end += 1

        return max_profit
        