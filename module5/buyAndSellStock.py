"""
Understand 
Must buy before you sell for max profit
[6,3,1,2,5,4] --> prices[4] - prices[2] = 5 - 1 = 4 
[8,5,3,1] --> In this case, no transactions are done and the max profit = 0.

Plan
Unbounded upper value for comparison
Iterate through list and subtract max from min
return sum
"""

def buyAndSellStock(prices):
    buy, ans = float('inf'), 0
    for p in prices:
        buy, ans = min(buy, p), max(ans, p-buy)
    return ans
