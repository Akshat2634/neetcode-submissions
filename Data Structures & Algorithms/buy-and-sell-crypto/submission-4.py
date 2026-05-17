class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxP = 0
        n = len(prices)
        for i in range(len(prices)):
            cp = prices[i]
            for j in range(i+1,n):
                sp = prices[j]
                profit = sp-cp
                maxP = max(maxP,profit)

        return maxP