/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     public int val;
 *     public TreeNode left;
 *     public TreeNode right;
 *     public TreeNode(int val=0, TreeNode left=null, TreeNode right=null) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
public class Solution {
    public int MaxDepth(TreeNode root) {
        if (root == null) {
            return 0;
        }
        LinkedList<(TreeNode, int)> stack = new();
        int max_depth = 0;
        stack.AddLast((root, 1));

        while(stack.Any()) {
            (var curr, var depth) = stack.Last.Value;
            stack.RemoveLast();
            if (curr.left != null) {
                stack.AddLast((curr.left, depth+1));
            }
            if (curr.right != null) {
                stack.AddLast((curr.right, depth+1));
            }

            max_depth = Math.Max(max_depth, depth);
        }
        return max_depth;
    }
}