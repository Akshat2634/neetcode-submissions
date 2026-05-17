class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        mxProfit = 0
        n = len(prices)

        for i in range(n):
            curr = prices[i]
            for j in range(i+1,n):
                sp = prices[j]
                profit = prices[j]-prices[i]
                mxProfit = max(mxProfit,profit)

        return mxProfit