#https://leetcode.com/problems/palindromic-substrings/
class Solution:
    def countSubstrings(self, s: str) -> int:
        res=1
        for i in range(1,len(s)):
            p1,p2 = i,i
            while 0<=p1<len(s) and 0<=p2<len(s) and s[p1]==s[p2]:
                p1-=1
                p2+=1
                res+=1
            p1,p2 = i-1,i
            while 0<=p1<len(s) and 0<=p2<len(s) and s[p1]==s[p2]:
                p1-=1
                p2+=1
                res+=1
        return res