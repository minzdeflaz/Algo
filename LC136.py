#https://leetcode.com/problems/single-number/submissions/1168895001/
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        xor_result = 0

        for num in nums:
            xor_result ^= num
        return xor_result