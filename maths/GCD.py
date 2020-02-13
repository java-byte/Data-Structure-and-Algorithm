'''
Greatest Common Divisor

Given 2 non negative integers m and n, find gcd(m, n)

GCD of 2 integers m and n is defined as the greatest integer g such that g is a divisor of both m and n. Both m and n fit in a 32 bit signed integer. 

m : 6
n : 9

GCD(m, n) : 3


Note: NOTE : DO NOT USE LIBRARY FUNCTIONS 

'''


    class Solution:
	# @param A : integer
	# @param B : integer
	# @return an integer
	def gcd(self, A, B):
	    if A<B:
	        return self.gcd(B,A)
	    if A==B==0:
	        return
	    if B==0:
	        return A
	    return self.gcd(B, A%B)

