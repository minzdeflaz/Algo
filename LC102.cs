//https://leetcode.com/problems/binary-tree-level-order-traversal/submissions/1208509829/
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
    public IList<IList<int>> LevelOrder(TreeNode root) {
        IList<IList<int>> res = new List<IList<int>>();
        if (root == null){
            return res;
        }
        LinkedList<(TreeNode, int)> queue = new();

        queue.AddLast((root, 0));


        while (queue.Any()){
            (var cur_node, var cur_level) = queue.First.Value;
            queue.RemoveFirst();

            if (res.Count == cur_level){
                res.Add(new List<int>(){cur_node.val});
            } else {
                res[cur_level].Add(cur_node.val);
            }

            if (cur_node.left != null){
                queue.AddLast((cur_node.left, cur_level+1));
            }

            if (cur_node.right != null){
                queue.AddLast((cur_node.right, cur_level+1));
            }
        }

        return res;
    }
}