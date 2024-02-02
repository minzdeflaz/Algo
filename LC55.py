#https://leetcode.com/problems/jump-game/
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        furthest = 0
        for i in range(len(nums)-1):
            if i > furthest:
                return False
            num = nums[i]
            furthest = max(furthest, num+i)
        return furthest >= len(nums)-1