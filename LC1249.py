#https://leetcode.com/problems/minimum-remove-to-make-valid-parentheses/
class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        st = collections.deque()

        remove = set()
        for i,c in enumerate(s):
            if c == "(":
                st.append(i)
            elif c == ")":
                if st:
                    st.pop()
                else:
                    remove.add(i)
        
        while st:
            remove.add(st.pop())
        res = ""
        for i,c in enumerate(s):
            if i in remove:
                continue
            res +=c
        return res                
            