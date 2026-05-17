class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mxProfit = 0
        for i in range(len(prices)):
            curr = prices[i]
            for j in range(i+1,len(prices)):
                sp = prices[j]
                profit = sp-curr
                mxProfit = max(mxProfit,profit)
        return mxProfit


