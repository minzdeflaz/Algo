#https://leetcode.com/problems/longest-repeating-character-replacement/description/
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        n = len(s)
        if n <2:
            return n
        max_length = 0
        repeat = {}
        left, right = 0,0
        max_freq = 0
        while right<n:
            repeat[s[right]] = repeat.get(s[right], 0) + 1
            max_freq = max(max_freq, repeat[s[right]])

            if right-left+1 - max_freq > k:
                repeat[s[left]] -=1
                left+=1
            else:
                max_length = max(max_length, right-left+1)
            right+=1
        return max_length

