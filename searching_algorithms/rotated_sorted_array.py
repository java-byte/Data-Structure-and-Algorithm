'''

Rotated Sorted Array Search

Given an array of integers A of size N and an integer B.

array A is rotated at some pivot unknown to you beforehand.

(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2 ).

You are given a target value B to search. If found in the array, return its index, otherwise return -1.

You may assume no duplicate exists in the array.

NOTE:- Array A was sorted in non-decreasing order before rotation.

        NOTE : Think about the case when there are duplicates. Does your current solution work? How does the time complexity change?*


Constraints

1 <= N <= 1000000
1 <= A[i] <= 10^9
all elements in A are disitinct.


nput 1:
    A = [4, 5, 6, 7, 0, 1, 2, 3]
    B = 4
Output 1:
    0
Explanation 1:
 Target 4 is found at index 0 in A.


Input 2:
    A = [5, 17, 100, 3]
    B = 6
Output 2:

'''


class Solution:
    # @param A : tuple of integers
    # @param B : integer
    # @return an integer
    def search_without_duplicates(self, A, B):
        n = len(A)
        start = 0; end = n-1
        
        while start<=end:
            
            mid = start + (end - start)//2
            
            if A[mid]==B:
                return mid
            if (A[mid]>=A[start] and B>=A[start]) or (A[mid]<A[start] and B<A[start]):
                if B>A[mid]:
                    start = mid+1
                else:
                    end = mid-1
            elif A[mid]>B:
                start = mid+1
            elif A[mid]<B:
                end = mid -1
        
        return -1

    def search_with_duplicates(self, A, B):
	n = len(A)
        start = 0; end = n-1
        
        while start<=end:
            
            mid = start + (end - start)//2
            
            if A[mid]==B:
                return mid
	    if A[start]==A[end]:
		end -= 1
 		continue
            if (A[mid]>=A[start] and B>=A[start]) or (A[mid]<A[start] and B<A[start]):
                if B>A[mid]:
                    start = mid+1
                else:
                    end = mid-1
            elif A[mid]>B:
                start = mid+1
            elif A[mid]<B:
                end = mid -1
        
        return -1
