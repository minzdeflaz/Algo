#https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/description/
class Solution:
    def findMin(self, nums) -> int:
        #[1,2,3,4,5]
        #[3,4,5,1,2]
        #[4,5,1,2,3]
        #[5,1,2,3,4]
        last_i = len(nums)-1
        start = 0
        end = last_i
        while start!=end:
            length = (end-start+1)
            mid = start + length//2
            if nums[start]<nums[end]:
                break
            elif nums[start]>nums[end]:
                if nums[mid] < nums[end]:
                    end =mid
                else:
                    start = mid
        return nums[start]