'''
Min XOR value

Problem Description
Given an integer array A of N integers, find the pair of integers in the array which have minimum XOR value. Report the minimum XOR value.



Input Format

First and only argument of input contains an integer array A.



Output Format

return a single integer denoting minimum xor value.



Example Input
Input 1:

A = [0, 2, 5, 7]

Input 2:

A = [0, 4, 7, 9]



Example Output
Output 1:

2

Output 2:

3



'''

    class Solution:
	# @param A : list of integers
	# @return an integer
	def findMinXor(self, A):
	    minVal = float('inf')
	    A.sort(); n = len(A)
	    for i in range(n-1):
	        minVal = min(minVal, A[i]^A[i+1])
	    return minVal

