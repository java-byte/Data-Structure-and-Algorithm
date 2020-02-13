'''

Xor queries

Problem Description
You are given an array A (containing only 0 and 1) as element of N length.

Given L and R, you need to determine value of XOR of all elements from L to R (both inclusive) and number of unset bits (0's) in the given range of the array.

Input Format

First argument contains the array of size N containing 0 and 1 only. 
Second argument contains a 2D array with Q rows and 2 columns, each row represent a query with 2 columns representing L and R.


Output Format

Return an 2D array of Q rows and 2 columns i.e the xor value and number of unset bits in that range respectively for each query.

'''

class Solution:
    # @param A : list of integers
    # @param B : list of list of integers
    # @return a list of list of integers
    def solve(self, A, B):
        n = len(A)
        xor_arr = [[None, None] for k in range(n)]
        xor = 0; count=0
        
        for i in range(n):
            xor = xor^A[i]
            xor_arr[i][0] = xor
            
            count+=A[i]
            xor_arr[i][1] = count
            
        result = []
        #print(xor_arr)
        for query in B:
            left, right = query[0], query[1]
            
            if left==1:
                val = xor_arr[right-1][0]
                oneCount = xor_arr[right-1][1]
                zeroCount = right - oneCount
                result.append([val, zeroCount])
            else:
                val = xor_arr[right-1][0]^xor_arr[left-2][0]
                oneCount = xor_arr[right-1][1] - xor_arr[left-2][1]
                zeroCount = right - left + 1 - oneCount
                result.append([val, zeroCount])
        return result





