#https://leetcode.com/problems/course-schedule/
from collections import deque
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = [set() for _ in range(numCourses)]
        for to, fromm in prerequisites:
            adj[fromm].add(to)

        stack = deque()
        visited = [False]*numCourses
        def toposort(v, adj, stack, visited):
            visited[v] = True
            for u in adj[v]:
                if not visited[u]:
                    toposort(u, adj, stack, visited)
            stack.appendleft(v)
        for v in range(numCourses):
            if not visited[v]:
                toposort(v, adj, stack, visited)
        
        seen = set()
        for course in stack:
            seen.add(course)
            if adj[course].intersection(seen):
                return False
        return True