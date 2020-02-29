'''
Unique Paths III

Problem Description

Given a matrix of integers A of size N x M . There are 4 types of squares in it:

1. 1 represents the starting square.  There is exactly one starting square.
2. 2 represents the ending square.  There is exactly one ending square.
3. 0 represents empty squares we can walk over.
4. -1 represents obstacles that we cannot walk over.

Find and return the number of 4-directional walks from the starting square to the ending square, that walk over every non-obstacle square exactly once.

Note: Rows are numbered from top to bottom and columns are numbered from left to right. 

Input Format

The first argument given is the integer matrix A.


Output Format

Return the number of 4-directional walks from the starting square to the ending square, that walk over every non-obstacle square exactly once.


Example Input

Input 1:

A = [   [1, 0, 0, 0]
        [0, 0, 0, 0]
        [0, 0, 2, -1]   ]

Input 2:

A = [   [0, 1]
        [2, 0]    ]



Example Output

Output 1:

2

Output 2:

0



Example Explanation

Explanation 1:

We have the following two paths: 
1. (0,0),(0,1),(0,2),(0,3),(1,3),(1,2),(1,1),(1,0),(2,0),(2,1),(2,2)
2. (0,0),(1,0),(2,0),(2,1),(1,1),(0,1),(0,2),(0,3),(1,3),(1,2),(2,2)


'''


class Solution:
    # @param A : list of list of integers
    # @return an integer
    def solve(self, A):
        row = len(A)
        if row==0: return 0
        col = len(A[0])
        
        self.count=0
        
        start_row, start_col = None, None
        zero_count = 0
        
        for i in range(row):
            for j in range(col):
                if A[i][j]==0:
                    zero_count+=1
                if A[i][j]==1:
                    start_row, start_col = i, j
        
        self.backTrack(A, start_row, start_col, zero_count)
        
        return self.count
    
    def backTrack(self, A, row, col, zero_count):
        if A[row][col]==2:
            if zero_count==0:
                self.count+=1
            return
        
        A[row][col]=-1
        
        X = [1, 0, -1, 0]
        Y = [0, 1, 0, -1]
        
        for i in range(4):
            new_row = row + Y[i]
            new_col = col + X[i]
            
            if self.isValid(A, new_row, new_col):
                
                if A[new_row][new_col]==0:
                    zero_count-=1
                self.backTrack(A, new_row, new_col, zero_count)
                
                if A[new_row][new_col]==0:
                    zero_count+=1
        
        A[row][col]=0
                
        
    def isValid(self, A, row, col):
        return row>=0 and row<len(A) and col>=0 and col<len(A[0]) and A[row][col]!=-1
        
        
        
        
        


