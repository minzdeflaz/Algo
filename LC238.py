# https://leetcode.com/problems/product-of-array-except-self/description/
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod = 1
        zero = False
        d_zero = False
        for num in nums:
            if num == 0:
                if zero:
                    d_zero = True
                else:
                    zero = True
                continue
            prod *= num

        if d_zero:
            return [0] * len(nums)
        res = []
        for num in nums:
            if zero:
                res.append(prod if num == 0 else 0)
            else:
                res.append(int(prod / num))
        return res
