'''
Combination Sum II

Problem Description

Given an array of size N of candidate numbers A and a target number B. Return all unique combinations in A where the candidate numbers sums to B.

Each number in A may only be used once in the combination.

Note:

    All numbers (including target) will be positive integers.
    Elements in a combination (a1, a2, … , ak) must be in non-descending order. (ie, a1 ≤ a2 ≤ … ≤ ak).
    The solution set must not contain duplicate combinations.

Warning:

DO NOT USE LIBRARY FUNCTION FOR GENERATING COMBINATIONS.

Example : itertools.combinations in python. If you do, we will disqualify your submission and give you penalty points.



Problem Constraints

1 <= N <= 20



Input Format

First argument is an integer array A denoting the collection of candidate numbers.
Second argument is an integer which represents the target number. 



Output Format

Return all unique combinations in A where the candidate numbers sums to B.



Example Input

Input 1:

A = [10, 1, 2, 7, 6, 1, 5]
B = 8



Example Output

Output 1:

[ [1 1 6 ]
  [1 2 5 ]
  [1 7 ] 
  [2 6 ] ]
'''


class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return a list of list of integers
    def combinationSum(self, A, B):
        n = len(A); self.target=B
        A.sort()
        
        self.result = []
        
        self.backTrack(A, [], 0, n, 0)
        
        return self.result
    
    def backTrack(self, arr, tmp, start, end, curr_sum):
        if curr_sum==self.target:
            if tmp not in self.result:
                self.result.append(tmp[:])
            return
        if start==end:
            return
        
        for i in range(start, end):
            if curr_sum+arr[i]>self.target:
                return
            
            tmp.append(arr[i])
            curr_sum += arr[i]
            
            self.backTrack(arr, tmp, i+1, end, curr_sum)
            
            tmp.pop()
            curr_sum -= arr[i]
    
            

