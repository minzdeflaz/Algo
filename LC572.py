#https://leetcode.com/problems/subtree-of-another-tree/
from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree_equal(self, root, subRoot):
        if not root and not subRoot:
            return True
        if not root or not subRoot or root.val != subRoot.val:
            return False
        return self.tree_equal(root.left, subRoot.left) and self.tree_equal(root.right, subRoot.right)
    def isSubtree(
        self, root: Optional[TreeNode], subRoot: Optional[TreeNode], first=True
    ) -> bool:
        queue = deque([root])
        while len(queue)>0:
            curr = queue.popleft()
            if curr.val == subRoot.val:
                res = self.tree_equal(curr, subRoot)
                if res:
                    return True
            if curr.left:
                queue.append(curr.left)
            if curr.right:
                queue.append(curr.right)
        return False