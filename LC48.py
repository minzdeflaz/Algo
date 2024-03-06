#https://leetcode.com/problems/rotate-image/
class Solution:
    def rotate(self, matrix: List[List[int]], start_i =0) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        """
          0 1 2
        0 1 2 3
        1 4 5 6
        2 7 8 9
        
          0 1 2
        0 7 4 1
        1 8 5 2
        2 9 6 3

        start_i = 0
        end_i = 2
        2,0 -> 0,0
        0,0 -> 0,2
        0,2 -> 2,2
        2,2 -> 2,0

        1,0 -> 0,1
        0,1 -> 1,2
        1,2 -> 2,1
        2,1 -> 1,0
        """
        # end = n//2
        # start_i from 0 -> n//2
        # at each start_i, index start at start_i
        # index: start_i -> length - start_i - 1
        end_i = len(matrix) - start_i - 1
        for i in range(end_i-start_i):
            start = matrix[start_i][i+start_i]
            matrix[start_i][start_i + i] = matrix[end_i-i][start_i]
            matrix[end_i-i][start_i] = matrix[end_i][end_i-i]
            matrix[end_i][end_i-i] =  matrix[start_i+i][end_i]
            matrix[start_i+i][end_i] = start
        if start_i < len(matrix)//2:
            self.rotate(matrix, start_i +1) 
        