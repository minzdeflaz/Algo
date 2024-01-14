#https://leetcode.com/problems/valid-parentheses/
from collections import deque
class Solution:
    brack_map = {
        ")":"(",
        "]":"[",
        "}":"{",
    }
    def isValid(self, s: str) -> bool:
        stack = deque()
        for i in s:
            if i not in self.brack_map:
                stack.append(i)
            else:
                if not stack or self.brack_map[i] != stack.pop():
                    return False
                    
        return not stack