# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        ancestors = {root:[root]}
        queue = [root]
        pFound, qFound = False, False
        while len(queue) > 0:
            cur = queue.pop(0)
            if cur.left != None:
                queue.append(cur.left)
                ancestors[cur.left] = ancestors[cur].copy()
                ancestors[cur.left].append(cur.left)
                pFound = True if cur.left == p else pFound
                qFound = True if cur.left == q else qFound
            if cur.right != None:
                queue.append(cur.right)
                ancestors[cur.right] = ancestors[cur].copy()
                ancestors[cur.right].append(cur.right)
                pFound = True if cur.right == p else pFound
                qFound = True if cur.right == q else qFound            
            if pFound and qFound:
                break
        pAnc = ancestors[p]
        qAnc = ancestors[q]
        s = pAnc
        l = qAnc
        if len(qAnc) < len(pAnc):
            s = qAnc
            l = pAnc
        for i in s[::-1]:
            for j in l[::-1]:
                if i == j:
                    return i