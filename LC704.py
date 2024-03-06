#https://leetcode.com/problems/binary-search/submissions/1182405521/
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        def bin_search(start,end,target):
            if not 0<=start<=end<len(nums):
                return -1
            mid = start+ (end-start+1)//2
            if target == nums[mid]:
                return mid

            elif target >nums[mid]:
                return bin_search(mid+1,end,target)
            else:
                return bin_search(start,mid-1,target)
        return bin_search(0, len(nums)-1, target)