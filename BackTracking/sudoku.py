'''
Problem Description

Write a program to solve a Sudoku puzzle by filling the empty cells. Empty cells are indicated by the character '.' You may assume that there will be only one unique solution.


'''

class Solution:
    # @param A : list of list of chars
    
    def available_digit(self, matrix, row, col):
        digit = {1,2,3,4,5,6,7,8,9}
        
        for i in range(9):
            if matrix[row][i]!='.':
                digit.discard(int(matrix[row][i]))
        
        for i in range(9):
            if matrix[i][col]!='.':
                digit.discard(int(matrix[i][col]))
        
        new_row = (row//3)*3
        new_col = (col//3)*3
        
        for i in range(new_row, new_row+3):
            for j in range(new_col, new_col+3):
                if matrix[i][j]!='.':
                    digit.discard(int(matrix[i][j]))
                    
        #print(digit)
        return digit
    
    def backTrack(self, A):
        
        for i in range(9):
            for j in range(9):
                if A[i][j]=='.':
                    option = self.available_digit(A, i, j)
                    
                    if len(option)==0:
                        return False
                    for digit in option:
                        A[i][j]=str(digit)
                        if self.backTrack(A):
                            return True
                        A[i][j] = '.'
                    return False
        
        return True
        
                        
        
    def solveSudoku(self, A):
       
        self.backTrack(A)
        
        
        
        
