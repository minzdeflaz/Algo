#https://leetcode.com/problems/longest-palindromic-substring/
class Solution:
    def longestPalindrome(self, s: str) -> str:
        def odd(p):
            p1,p2 = p-1,p+1
            while 0<=p1<len(s) and 0<=p2<len(s) and s[p1]==s[p2]:
                p1-=1
                p2+=1
            return s[p1+1:p2]
        def even(p1,p2):
            if s[p1]!=s[p2]:
                return ""
            while 0<=p1<len(s) and 0<=p2<len(s) and s[p1]==s[p2]:
                p1-=1
                p2+=1
            return s[p1+1:p2]
        maxx = odd(0)
        for i in range(1,len(s)):
            maxx = max(maxx, odd(i), even(i-1,i), key=lambda x:len(x))
        return maxx