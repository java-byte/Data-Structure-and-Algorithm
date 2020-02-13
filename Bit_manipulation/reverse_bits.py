'''

Problem Description

Reverse the bits of an 32 bit unsigned integer A.

Input Format
First and only argument of input contains an integer A.

Output Format
Return a single unsigned integer denoting minimum xor value.




'''

class Solution:
    # @param A : unsigned integer
    # @return an unsigned integer
    def reverse(self, A):
        ans = 0
        
        i = 0
        while A>0:
            
            if A&1:
                ans = ans + 2**(31-i)
            i+=1
            A>>=1
        return ans
	
