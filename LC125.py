#https://leetcode.com/problems/valid-palindrome/submissions/1182409228/
class Solution:
    def isPalindrome(self, s: str) -> bool:
        l = 0
        r = len(s)-1
        while l<=r:
            if not s[l].isalnum():
                l+=1
                continue
            if not s[r].isalnum():
                r-=1
                continue
            
            if s[l].lower() != s[r].lower():
                return False
            else:
                r-=1
                l+=1
        return True