#https://leetcode.com/problems/count-nodes-equal-to-average-of-subtree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: TreeNode) -> int:
        res = 0

        def recur(node):
            nonlocal res
            if not node:
                return 0,0

            l_sum, l_count = recur(node.left)
            r_sum, r_count = recur(node.right)

            c_sum = l_sum + r_sum + node.val
            c_count = l_count + r_count +1

            if int(c_sum/c_count) == node.val:
                res+=1
            return c_sum, c_count
            
        recur(root)
        return res
            
