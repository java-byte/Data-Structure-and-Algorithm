'''
The n-queens puzzle is the problem of placing n queens on an n×n chessboard such that no two queens attack each other.

Given an integer n, return all distinct solutions to the n-queens puzzle.

Each solution contains a distinct board configuration of the n-queens' placement, where 'Q' and '.' both indicate a queen and an empty space respectively.

Example Input

Input 1:

n = 4



Example Output

Output 1:

[
 [".Q..",  // Solution 1
  "...Q",
  "Q...",
  "..Q."],

 ["..Q.",  // Solution 2
  "Q...",
  "...Q",
  ".Q.."]
]

'''

from copy import copy, deepcopy
class Solution:
    # @param A : integer
    # @return a list of list of strings
    
    def isValid(self, row, col):
        if row in self.row or col in self.col :
            return False
        
        left_diagonal = row-col
        right_diagonal = row+col
        
        if left_diagonal in self.diagonal_left or right_diagonal in self.diagonal_right:
            return False
        
        return True
        
        
    def solveNQueens(self, A):
        if A==3 or A==2:
            return []
        if A==1:
            return ['Q']
        
        matrix = [['.' for i in range(A)] for j in range(A)]
        
        self.row = set(); self.col = set(); self.diagonal_left = set(); self.diagonal_right = set()
        
        self.result = set(); self.n = A
        
        self.backTrack(matrix, 0, 0)
        
        #print("result: ", self.result)
        
        self.result = list(map(list, self.result))
        for res in self.result:
            for val in range(len(res)):
                res[val] = "".join(res[val])
                
        return self.result
        
    
    def backTrack(self, matrix, r, queen_count):
       
        if queen_count==self.n:
            #print("matrix: ",matrix)
            self.result.add(tuple(map(tuple,deepcopy(matrix))))
            return
        if r==self.n:return
        
        for j in range(self.n):
            if matrix[r][j]=='.' and self.isValid(r, j):
                matrix[r][j]='Q'
                self.row.add(r)
                self.col.add(j)
                self.diagonal_left.add(r-j)
                self.diagonal_right.add(r+j)

                self.backTrack(matrix, r+1, queen_count+1)

                matrix[r][j]='.'
                self.row.discard(r)
                self.col.discard(j)
                self.diagonal_left.discard(r-j)
                self.diagonal_right.discard(r+j)
