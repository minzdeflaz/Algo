//https://leetcode.com/problems/diameter-of-binary-tree/submissions/1196144932/
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
    public int DiameterOfBinaryTree(TreeNode root) {
        int maxLength = 0;
        int helper(TreeNode node) {
            if (node.left == null && node.right == null){
                return 0;
            }

            int left = node.left == null? 0: helper(node.left)+1;
            int right = node.right == null? 0: helper(node.right)+1;
            maxLength = Math.Max(left+right, maxLength);
            return Math.Max(left, right);
        }
        if (root!= null){
            helper(root);
        }
        return maxLength;
    }
}