#https://leetcode.com/problems/search-in-rotated-sorted-array/description/
class Solution:
    def search(self, nums, target: int) -> int:
        left, right = 0, len(nums)-1        
        while left<=right:
            mid = left + (right-left +1)//2
            if nums[mid] == target:
                return mid
            if nums[left] == target:
                return left
            if nums[right] == target:
                return right
            
            if nums[left] < nums[right]:
                if target >nums[mid]:
                    left = mid+1
                else:
                    right = mid-1
            else:
                if target >nums[mid] > nums[left] or nums[mid] <target < nums[right]:
                    left = mid+1
                elif nums[mid]>target>nums[left] or target<nums[mid]<nums[right]:
                    right = mid-1
            print(left, right, mid)
            print(nums[mid],target,nums[left])
        return -1
    
a = Solution()
a.search( nums = [4,5,6,7,0,1,2], target = 0)