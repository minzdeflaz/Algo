# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buyIdx = 0
        sellIdx = 0
        maxProf = 0
        while sellIdx < len(prices):
            prof = prices[sellIdx] - prices[buyIdx]
            if prof > 0:
                maxProf = max(prof, maxProf)
            else:
                buyIdx = sellIdx
            sellIdx += 1
        return maxProf
