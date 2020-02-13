'''

Single Number

Problem Description
Given an array of integers, every element appears twice except for one. Find that single one.

Note: Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

Input Format
First and only argument of input contains an integer array A.


Output Format
Return a single integer denoting the single element.

Input:1
A = [1, 2, 2, 3, 1]
output: 3

Input:2
A = [1, 2, 2]
output: 1


'''

class Solution:
    # @param A : tuple of integers
    # @return an integer
    def singleNumber(self, A):
        xor = 0
	for i in range(len(A)):
	     xor = xor^A[i]
	return xor

