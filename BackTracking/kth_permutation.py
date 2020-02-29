'''
Kth Permutation Sequence

The set [1,2,3,…,n] contains a total of n! unique permutations.

By listing and labeling all of the permutations in order, We get the following sequence (ie, for n = 3 ) :

1. "123"
2. "132"
3. "213"
4. "231"
5. "312"
6. "321"

Given n and k, return the kth permutation sequence.

For example, given n = 3, k = 4, ans = "231"

    Good questions to ask the interviewer :

        What if n is greater than 10. How should multiple digit numbers be represented in string?

        In this case, just concatenate the number to the answer. so if n = 11, k = 1, ans = "1234567891011" 

        Whats the maximum value of n and k?

        In this case, k will be a positive integer thats less than INT_MAX. n is reasonable enough to make sure the answer does not bloat up a lot. 


'''

class Solution:
	# @param A : integer
	# @param B : integer
	# @return a strings
	
	'''
	def backTrack(self, arr, start, end):
	    if start==end:
	        self.result.append("".join(arr[:]))
	        return
	    
	    for i in range(start, end):
	        arr[i], arr[start] = arr[start], arr[i]
	        self.backTrack(arr, start+1, end)
	        
	        arr[i], arr[start] = arr[start], arr[i]
	        
	def getPermutation(self, A, B):
	    
	    arr = [str(i) for i in range(1, A+1)]
	    
	    self.result = []
	    
	    self.backTrack(arr, 0, len(arr))
	    
	    self.result.sort()
	    return "".join(self.result[B-1])
	'''
	def fact(self, n):
	    if n==1:
	        return 1
	    return n*self.fact(n-1)
	    
	def getPermutation(self, A, B):
	    n = A
	    
	    arr = [i for i in range(1, n+1)]
	    
	    final = []
	    while n>1:
	        val = math.ceil(B/self.fact(n-1))
	        final.append(str(arr[val-1]))
	        n = n-1
	        B = B-(val-1)*(self.fact(n))
	        arr.pop(val-1)
	    final.append(str(arr[0]))
	    return "".join(final)
	    
	    
	    
	    
	    
	    
	    

