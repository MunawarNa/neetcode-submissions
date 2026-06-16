class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        
        start = 0
        end = 0
        mx_profit = 0
        
        while end < len(prices):
            if prices[start] < prices[end]:
                mx_profit = max(mx_profit, prices[end] - prices[start])
            else:
                start = end 
            end += 1
        return mx_profit



            