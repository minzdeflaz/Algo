class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        if n<2:
            return n
        start = 0

        res = 0
        seen = set()
        end = start
        while start < n:
            if end<n and s[end] not in seen:
                seen.add(s[end])
                end+=1
            else:
                res = max(res, len(seen))
                seen = set()
                start+=1
                end = start
        res = max(res, len(seen))
        return res
#https://leetcode.com/problems/longest-substring-without-repeating-characters/