# https://leetcode.com/problems/validate-binary-search-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        MIN = -2**31 - 1
        MAX = 2**31
        def validateBST(node, curMin, curMax):
            if node == None:
                return True
            if curMin < node.val and curMax > node.val:
                return validateBST(node.left, curMin, node.val) and validateBST(node.right, node.val, curMax)
            return False
        return validateBST(root, MIN, MAX)