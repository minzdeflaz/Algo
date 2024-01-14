#https://leetcode.com/problems/3sum/
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        length = len(nums)
        output = []
        for k in range(length-2):
            if k>0 and nums[k] == nums[k-1]:
                continue
            i = k+1
            j = length - 1
            while i<j:
                
                summ = nums[k]+nums[i]+nums[j]
                if summ == 0:
                    while i+1<j and nums[i]==nums[i+1]:
                        i+=1
                    while j-1>i and nums[j]==nums[j-1]:
                        j-=1
                    output.append([nums[k], nums[i], nums[j]])
                    i+=1
                    j-=1
                elif summ >0:
                    j-=1
                else: 
                    i+=1
        return output
                    