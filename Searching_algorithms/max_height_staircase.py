'''
Maximum height of the staircase

Given an integer A representing the square blocks. The height of each square block is 1. The task is to create a staircase of max height using these blocks.

The first stair would require only one block, the second stair would require two blocks and so on.

Find and return the maximum height of the staircase.


Input Format

The only argument given is integer A.

Output Format

Return the maximum height of the staircase using these blocks.

Constraints

0 <= A <= 10^9

For Example

Input 1:
    A = 10
Output 1:
    4

Input 2:
    A = 20
Output 2:
    5


'''


class Solution:
    # @param A : integer
    # @return an integer
    def findSum(self, num):
        if num<=0:
            return 0
        
        val = (num/2)*(1 + num)
        
        return val
        
    def solve(self, A):
        
        start = 1; end = A; candidate = None
        
        while start<=end:
            mid = start + (end - start)//2
            
            midVal = mid + self.findSum(mid-1)
            
            if midVal==A:
                return mid
            elif midVal<A:
                candidate = mid
                start = mid+1
            else:
                end = mid-1
        
        return candidate if candidate!=None else 0
            
