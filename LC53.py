#https://leetcode.com/problems/maximum-subarray/submissions/1157671153/
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        best = nums[0]
        cur = 0
        for num in nums:
            cur+=num
            best = max(best, cur)
            if cur < 0:
                cur = 0
        return best