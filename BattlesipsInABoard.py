# https://leetcode.com/problems/battleships-in-a-board/
from typing import List

class Solution:
    
    def countBattleships(self, board: List[List[str]]) -> int:
        row = len(board)
        col = len(board[0])
        def checkBoard(board, i, j, isVertical):
            if board[i][j] == "X":
                if isVertical and i + 1 < row:
                    checkBoard(board, i + 1, j, isVertical)
                if not isVertical and j + 1 < col:
                    checkBoard(board, i, j + 1, isVertical)
                board[i][j] = "."
                return True
            else:
                return False
        ships = 0
        if row == 1 and col == 1:
            return 1 if board[0][0] == "X" else 0
        for i in range(row):
            for j in range(col):
                if board[i][j] == "X":
                    if i + 1 < row and board[i+1][j] == "X":
                        checkBoard(board, i + 1, j, True)
                    elif j + 1 < col and board[i][j+1] == "X":
                        checkBoard(board, i, j + 1, False)
                    ships += 1
        return ships
