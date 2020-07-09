#Input: [7,1,5,3,6,4]
#Output: 5
#Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
#             Not 7-1 = 6, as selling price needs to be larger than buying price.

class Solution(object):
    def maxProfit(self, prices):
        low = float('inf')
        profit = 0
        for price in prices:
            profit = max(profit, price-low)
            low = min(low, price)
        return profit
