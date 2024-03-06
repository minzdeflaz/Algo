#https://leetcode.com/problems/diameter-of-n-ary-tree/
"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children if children is not None else []
"""

class Solution:
    max_length = 0
    def diameter(self, root: 'Node') -> int:
        """
        :type root: 'Node'
        :rtype: int
        """
        def recur(node):
            child_heights = [0,0]
            heapq.heapify(child_heights)
            
            for child in node.children:
                height = recur(child)
                heapq.heappush(child_heights, -(height+1))
            first, second = -heapq.heappop(child_heights), -heapq.heappop(child_heights)
            self.max_length = max(self.max_length, first+second)
            return first
        recur(root)
        return self.max_length
