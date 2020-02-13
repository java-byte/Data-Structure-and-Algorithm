'''

Given two integers dividend and divisor, divide two integers without using multiplication, division and mod operator.

Return the quotient after dividing dividend by divisor.

The integer division should truncate toward zero.

Example 1:

Input: dividend = 10, divisor = 3
Output: 3

Example 2:

Input: dividend = 7, divisor = -3
Output: -2

Note:

    Both dividend and divisor will be 32-bit signed integers.
    The divisor will never be 0.
    Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−231,  231 − 1]. For the purpose of this problem, assume that your function returns 231 − 1 when the division result overflows.




'''

class Solution:
    def divide(self, A: int, B: int) -> int:
        
        if A==0:
	        return 0
        sign = None
        if (A<0 and B<0) or (A>0 and B>0):
	        sign = 1
	        if abs(A)==2147483648 and abs(B)==1:
	            return 2147483647
        else:
            sign = -1
        divd = abs(A); divs = abs(B); ans=0
        while divd>=divs:
            count = 1; res = divd; tmpDivs = divs
            while res>=0:
	            res = (divd - (tmpDivs << 1))
	            if res <0:
	                break
	            count <<= 1
	            tmpDivs <<= 1
            ans += count
            divd = divd - tmpDivs
        return sign*ans
