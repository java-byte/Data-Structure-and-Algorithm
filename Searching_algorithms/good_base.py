'''
Smallest Good Base

Given an integer A, we call k >= 2 a good base of A, if all digits of A base k are 1. Now given a string representing A, you should return the smallest good base of A in string format.


Input Format

The only argument given is the string representing A.

Output Format

Return the smallest good base of A in string format.

Constraints

3 <= A <= 10^18

For Example

Input 1:
    A = "13"
Output 1:
    "3"     (13 in base 3 is 111)

Input 2:
    A = "4681"
Output 2:
    "8"     (4681 in base 8 is 11111).




'''

class Solution:
    # @param A : string
    # @return a strings
    
    def findSum(self, mid, i):
        ## G.P. Sum
        return (mid**i - 1)//(mid - 1)
        
    def solve(self, A):
        A = int(A)
        for i in range(64,0,-1):
            candidate = None
            start = 2; end = A -1
            
            while start<=end:
                mid = start + (end - start)//2
                
                currSum = self.findSum(mid, i)
                if currSum==A:
                    #candidate = mid
                    #end = mid-1
                    return str(mid)
                elif currSum>A:
                    end = mid-1
                else:
                    start = mid+1
            
            if candidate==None:
                continue
            else:
                return str(candidate)
                
