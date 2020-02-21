'''
Special Integer

Given an array of integers A and an integer B, find and return the maximum value K such that there is no subarray in A of size K with sum of elements greater than B.


Input Format

The first argument given is the integer array A.
The second argument given is integer B.

Output Format

Return the maximum value of K (sub array length).

Constraints

1 <= length of the array <= 100000
1 <= A[i] <= 10^9
1 <= B <= 10^9

For Example

Input 1:
    A = [1, 2, 3, 4, 5]
    B = 10
Output 1:
    2

Input 2:
    A = [5, 17, 100, 11]
    B = 130
Output 2:
    3

'''


class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    
    def findSum(self, arr, start, end):
        if start==0:
            return arr[end]
        else:
            return arr[end]-arr[start-1]
            
    def solve(self, A, B):
        n = len(A)
        maxVal = max(A)
        if maxVal>B:
            return 0
        if maxVal==B:
            return 1
        
        prefix = [0]*n
        for i in range(n-1):
            prefix[i+1] = A[i+1]+prefix[i]
        
        start = 1; end=n; K=None; minRange = 0
        while start<=end:
            mid = start + (end - start)//2
            
            K = mid; flag=True
            for i in range(0, n-(K-1)):
                sIndex = i; eIndex = i+K-1
                rangeSum = self.findSum(prefix, sIndex, eIndex)
                if rangeSum>B:
                    flag = False
                    break
            if flag==False:
                end = mid-1
            elif flag:
                minRange = max(minRange, K)
                start = mid+1
        
        return minRange
