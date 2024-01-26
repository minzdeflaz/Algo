#https://leetcode.com/problems/combination-sum/
from collections import deque
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        q = deque([[]])
        index_map = {val:i for i, val in enumerate(candidates)}
        res = []
        while q:
            curr = q.popleft()
            summ = sum(curr)
            if summ == target:
                res.append(curr)
                continue
            elif summ>target:
                continue
            if curr:
                i = index_map[curr[-1]]
            else:
                i = 0

            for j in range(i, len(candidates)):
                val = candidates[j]
                if summ + val <= target:
                    q.append(curr + [val])
        return res