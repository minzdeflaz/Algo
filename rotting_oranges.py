# https://leetcode.com/problems/rotting-oranges/
from collections import defaultdict

diff = [(0, -1), (0, 1), (-1, 0), (1, 0)]


def find_adj(grid, i, j):
    res = []
    for add_x, add_y in diff:
        new_x = i + add_x
        new_y = j + add_y
        if -1 < new_x < len(grid) and -1 < new_y < len(grid[0]):
            res.append((new_x, new_y))
    return res


def solution(grid: list[list[int]]) -> int:
    tomato_grid = defaultdict(lambda: -2)
    queue = []
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            val = grid[i][j]
            if val == 1:
                tomato_grid[(i, j)] = -1
            if val == 2:
                tomato_grid[(i, j)] = 0
                queue.append((i, j))

    while len(queue) != 0:
        i, j = queue.pop(0)
        adjs = find_adj(grid, i, j)
        for x, y in adjs:
            if tomato_grid[(x,y)] == -1:
                tomato_grid[(x,y)]= tomato_grid[(i,j)]+1
                queue.append((x,y))
    max_val = 0
    for val in tomato_grid.values():
        max_val = max(val, max_val)
        if val==-1:
            return -1
    return max_val
if __name__ == "__main__":
    tests = [
        ([[2, 1, 1], [1, 1, 0], [0, 1, 1]], 4),
        ([[2, 1, 1], [1, 1, 1], [1, 1, 1]], 4),
        ([[2, 1, 1], [1, 1, 1], [1, 1, 2]], 2),
        ([[1, 0, 1], [0, 2, 0], [1, 0, 1]], -1),
        ([[2, 1, 1], [0, 1, 1], [1, 0, 1]], -1),
    ]
    for test, result in tests:
        if (sol:=solution(test)) == result:
            print(f"test passed:{test}=> {result}")
        else:
            print(f"test failed:{test}=> {sol} instead of {result}")
