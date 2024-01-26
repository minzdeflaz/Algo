#https://leetcode.com/problems/reverse-linked-list/
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from collections import deque
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        stack = deque()
        curr = head
        while curr:
            stack.append(curr.val)
            curr = curr.next
        head = ListNode(stack.pop())
        curr = head
        while stack:
            curr.next = ListNode(stack.pop())
            curr = curr.next
        return head