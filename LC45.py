#https://leetcode.com/problems/jump-game-ii/submissions/1157789753/
class Solution:
    def jump(self, nums: List[int]) -> int:
        furthest = 0
        step_end = 0
        step = 0
        for i in range(len(nums)-1):
            furthest = max(furthest,nums[i]+i)
            if i == step_end:
                step+=1
                step_end = furthest
        return step
            