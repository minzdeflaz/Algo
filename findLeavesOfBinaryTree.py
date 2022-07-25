#https://leetcode.com/problems/find-leaves-of-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findLeaves(self, root: Optional[TreeNode]) -> List[List[int]]:
        nodesHeight = []
        def getNodeHeight(node: TreeNode):
            if node == None:
                return -1
            
            leftHeight = getNodeHeight(node.left)
            rightHeight = getNodeHeight(node.right)

            curHeight = max(leftHeight, rightHeight) + 1

            nodesHeight.append((curHeight, node.val))

            return curHeight
        
        getNodeHeight(root)

        nodesHeight.sort(key=lambda item: item[0])
        result = []
        for height, val in nodesHeight:
            if len(result) - 1 == height:
                result.append([])
            result[height].append(val)
        return result