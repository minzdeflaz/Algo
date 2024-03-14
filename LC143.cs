//https://leetcode.com/problems/reorder-list/submissions/1203180993/
/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     public int val;
 *     public ListNode next;
 *     public ListNode(int val=0, ListNode next=null) {
 *         this.val = val;
 *         this.next = next;
 *     }
 * }
 */
public class Solution {
    public void ReorderList(ListNode head) {
        LinkedList<ListNode> deque = new();

        while (head!=null){
            deque.AddLast(head);
            head = head.next;
        }
        bool isOdd = true;
        head = new();
        var curr = head;
        while (deque.Any()) {
            if (isOdd){
                curr.next = deque.First.Value;
                deque.RemoveFirst();
            } else {
                curr.next = deque.Last.Value;
                deque.RemoveLast();
            }
            isOdd = !isOdd;
            curr = curr.next;
        }
        curr.next = null;
        head = head.next;

    }
}