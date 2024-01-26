#https://leetcode.com/problems/clone-graph/description/
"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
from collections import defaultdict, deque
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return node
        visited = defaultdict(lambda: False)
        adj_map = defaultdict(list)
        q = deque([node])

        while q:
            curr = q.pop()
            if visited[curr.val]:
                continue
            visited[curr.val] = True
            #init
            adj_map[curr.val]
            for nxt in curr.neighbors:
                adj_map[curr.val].append(nxt.val)
                if not visited[nxt.val]:
                    q.appendleft(nxt)
        created = defaultdict(lambda:None)
        for val, adjs in adj_map.items():
            if not created[val]:
                created[val] = Node(val)
            for adj in adjs:
                if not created[adj]:
                    created[adj] = Node(adj)
                created[val].neighbors.append(created[adj])
        return created[1]