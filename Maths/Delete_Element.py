'''
Delete Elements

Problem Description
Given an integer array A of size N.
Find the minimum number of elements that need to be removed such that the GCD of the resulting array becomes 1.

If not possible then return -1.

Input-1:  A = [7, 2, 5]
Ouput: 0

GCD of the array A is 1.
so, the number of elements to be removed is 0.


'''

class Solution:
    # @param A : list of integers
    # @return an integer
    
    def gcd(self, a, b):
        if a<b:
            return self.gcd(b,a)
            
        if a==b==0:
            return
        if b==0:
            return a
        
        return self.gcd(b, a%b)
        
        
    def solve(self, A):
        n = len(A)
        
        ans = A[0]
        for i in range(1, n):
            ans = self.gcd(ans, A[i])
        
        if ans==1:
            return 0
        else:
            return -1



## Approach: If GCD is already 1 then we don't need to remove any element, else even we remove any element remaining element will always be divisible by GCD, because that's the property of GCD.
