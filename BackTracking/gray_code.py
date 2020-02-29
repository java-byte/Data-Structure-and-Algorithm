'''
Gray Code

Problem Description

The gray code is a binary numeral system where two successive values differ in only one bit.

Given a non-negative integer n representing the total number of bits in the code, print the sequence of gray code.

A gray code sequence must begin with 0.



Problem Constraints

1 <= n <= 16


Input Format

First argument is an integer n.


Output Format

Return an array of integers representing the gray code sequence.


Example Input

Input 1:

2



Ex

ample Output

output 1:

[0,1,3,2]



Example Explanation

Explanation 1:

for n = 2 the gray code sequence is:
    00 - 0
    01 - 1
    11 - 3
    10 - 2
So, return [0,1,3,2].

'''

class Solution:
    # @param A : integer
    # @return a list of integers
    def grayCode(self, A):
        arr = [0,1]
        if A==1:
            return arr
        
        while A>1:
            
            tmp = []
            n = len(arr)
            for i in range(n):
                tmp.append(arr[i]<<1)
            
            for i in range(n-1, -1, -1):
                tmp.append((arr[i]<<1)+1)
            
            arr = tmp
            A = A-1
        
        return arr
        






