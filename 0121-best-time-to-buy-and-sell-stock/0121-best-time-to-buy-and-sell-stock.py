class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        
        buy = 0
        sell = 0
        
        max_profit = 0
        while sell < len(prices):

            if prices[sell] < prices[buy]:
                buy = sell    
            else:
                max_profit = max(prices[sell]-prices[buy], max_profit)
            
            sell += 1
        return max_profit