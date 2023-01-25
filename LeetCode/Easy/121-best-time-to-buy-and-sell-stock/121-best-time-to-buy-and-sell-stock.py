class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        price_min = 10000 
        profit = 0 
        
        for price_current in prices:
            price_min = min(price_current, price_min)
            profit = max(profit, price_current-price_min) 
        return profit