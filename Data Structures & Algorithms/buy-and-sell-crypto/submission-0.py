class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        maxProfit = 0
        for i in range(n):
            buy = prices[i]
            for j in range(i+1,n):
                sell = prices[j]
                profit = sell-buy
                maxProfit = max(maxProfit,profit)
        return maxProfit

        