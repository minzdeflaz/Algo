#https://leetcode.com/problems/binary-tree-vertical-order-traversal/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, col=0, left=None, right=None):
#         self.col = col
#         self.left = left
#         self.right = right
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        res = collections.defaultdict(list)
        q = collections.deque()

        q.append((root,0))

        while q:
            cur, col = q.popleft()

            res[col].append(cur.val)
            
            if cur.left:
                q.append((cur.left, col-1))
            if cur.right:
                q.append((cur.right, col+1))
        out = []
        for col in sorted(res):
            out.append(res[col])
        
        return out
