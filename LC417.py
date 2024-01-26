#https://leetcode.com/problems/pacific-atlantic-water-flow/description/
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])

        pac_visit, alt_visit = set(), set()

        def expand(r, c, visited, prev_h=0):
            if (
                not (0 <= r < ROWS)
                or not (0 <= c < COLS)
                or (r, c) in visited
                or prev_h > heights[r][c]
            ):
                return
            visited.add((r, c))
            expand(r - 1, c, visited, heights[r][c])
            expand(r + 1, c, visited, heights[r][c])
            expand(r, c - 1, visited, heights[r][c])
            expand(r, c + 1, visited, heights[r][c])

        for r in range(ROWS):
            expand(r, 0, pac_visit)
            expand(r, COLS - 1, alt_visit)
        for c in range(COLS):
            expand(0, c, pac_visit)
            expand(ROWS - 1, c, alt_visit)
        res = []
        for r, c in alt_visit.intersection(pac_visit):
            res.append([r, c])
        return res
