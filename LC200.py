# https://leetcode.com/problems/number-of-islands/
from collections import deque

direction = [(0, -1), (0, 1), (-1, 0), (1, 0)]

class Solution:
    def bfs(self, grid, row, col, visited):
        stack = deque([(row, col)])

        while stack:
            row, col = stack.pop()
            visited[row][col] = True
            for x, y in direction:
                x_n = row + x
                y_n = col + y
                if 0 <= x_n < self.width and 0 <= y_n < self.height:
                    if not visited[x_n][y_n]:
                        stack.append((x_n, y_n))

    def numIslands(self, grid: List[List[str]]) -> int:
        self.width = len(grid)
        self.height = len(grid[0])
        visited = [[(cell == "0") for cell in row] for row in grid]
        island = 0
        for row in range(self.width):
            for col in range(self.height):
                if not visited[row][col]:
                    print(row, col)
                    self.bfs(grid, row, col, visited)
                    island += 1
        return island
