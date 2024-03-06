#https://leetcode.com/problems/number-of-1-bits/submissions/1168917148/
class Solution:
    def hammingWeight(self, n: int) -> int:
        total = 0
        while n !=0:
            if n%2:#odd
                total+=1
            n>>=1
        return total