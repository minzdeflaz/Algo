# https://leetcode.com/problems/two-sum/

from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        res = []
        sumDict = {}
        for i in range(len(nums)):
            cur = nums[i]
            if cur in sumDict.keys():
                res.append(sumDict[cur])
                res.append(i)
                return res
            else:
                sumDict[target - cur] = i
            print(sumDict)
        print(res)
        
        
if __name__ == "__main__":
    a = Solution()
    a.twoSum([2,7,11,15], 9)