#link: https://leetcode.com/problems/climbing-stairs/
class Solution:
    def __init__(self):
        self.ways = 1
    def climbStairs(self, n: int) -> int:
        def climb(n: int, stepsTaken = 0):
            if stepsTaken < n - 1:
                self.ways += 1
                climb(n, stepsTaken+1)
                climb(n, stepsTaken+2)
            elif stepsTaken + 1 == n:
                self.ways += 0
                climb(n, stepsTaken+1)
        climb(n)
        return self.ways
