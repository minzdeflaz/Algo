#https://leetcode.com/problems/coin-change/
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [amount +1] *(amount+1)

        dp[0] = 0
        for i in range(1, len(dp)):
            for c in coins:
                if i >=c:
                    dp[i] = min(dp[i-c]+1, dp[i])
        
        return dp[amount] if dp[amount] <amount+1 else -1
            