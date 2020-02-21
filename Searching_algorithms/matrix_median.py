'''
Matrix Median

Given a matrix of integers A of size N x M in which each row is sorted.

Find an return the overall median of the matrix A.

Note: No extra memory is allowed.

Note: Rows are numbered from top to bottom and columns are numbered from left to right.


Input Format

The first and only argument given is the integer matrix A.

Output Format

Return the overall median of the matrix A.


Input 1:
    A = [   [1, 3, 5],
            [2, 6, 9],
            [3, 6, 9]   ]
Output 1:
    5
Explanation 1:
    A = [1, 2, 3, 3, 5, 6, 6, 9, 9]
    Median is 5. So, we return 5.

Input 2:
    A = [   [5, 17, 100]    ]
Output 2:
    17


'''


class Solution:
    def findLessCount(self, A, target):
        count = 0
        for i in range(len(A)):
            arr = A[i]; candidate = None
            start = 0; end = len(arr) -1
            while start<=end:
                mid = start + (end - start)//2
                if arr[mid]<=target:
                    candidate = mid
                    start = mid+1
                else:
                    end = mid-1
            if candidate==None:
                count+=0
            else:
                count += (candidate+1)
        return count
    def findMedian(self, A):
        row = len(A)
        if row==0:
            return 0
        col = len(A[0])
        max_num = -float('inf'); min_num = float('inf')
        for i in range(row):
            max_num = max(max_num, A[i][col-1])
            min_num = min(min_num, A[i][0])
        
        lessCount = 0; moreCount = 0
        totalCount = row*col; target = (totalCount+1)//2
        while min_num<=max_num:
            mid = min_num + (max_num - min_num)//2
            lessCount = self.findLessCount(A, mid)
            if lessCount<target:
	            min_num = mid+1
            else:
	            max_num = mid-1
        return max_num+1


