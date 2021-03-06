'''
Single Element in a Sorted Array

Given a sorted array of integers A where every element appears twice except for one element which appears once, find and return this single element that appears only once.


Input Format

The only argument given is the integer array A.

Output Format

Return the single element that appears only once.

Constraints

1 <= length of the array <= 100000
1 <= A[i] <= 10^9 

For Example

Input 1:
    A = [1, 1, 2, 2, 3]
Output 1:
    3

Input 2:
    A = [5, 11, 11, 100, 100]
Output 2:
    5


'''

class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, arr):
        
        n = len(arr)
        start = 0; end = n-1
        
        while start< end:
            mid = start + (end - start)//2
            
            if (mid%2==0 and mid+1<n and arr[mid]==arr[mid+1]) or (mid%2!=0 and mid-1>=0 and arr[mid]==arr[mid-1]):
                start = mid+1
            else:
                end = mid
        
        return arr[end]
