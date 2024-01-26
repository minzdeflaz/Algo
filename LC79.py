#https://leetcode.com/problems/word-search/description/
directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        visited = set()
        def backtrack(board, i, j, word, w_id):
            if w_id == len(word) or (w_id == len(word)-1 and board[i][j] == word[w_id]):
                return True
            if board[i][j] != word[w_id]:
                return False
            visited.add((i,j))
            res = False
            for x, y in directions:
                x_n, y_n = i + x, j + y
                if 0 <= x_n < len(board) and 0 <= y_n < len(board[0]) and (x_n, y_n) not in visited:
                    res = res or backtrack(
                        board,
                        x_n,
                        y_n,
                        word,
                        w_id + 1,
                    )
            visited.remove((i,j))
            return res
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if backtrack(board, i, j, word, 0):
                    return True
        return False
