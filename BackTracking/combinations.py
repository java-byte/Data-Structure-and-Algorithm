'''
Combinations

Given two integers n and k, return all possible combinations of k numbers out of 1 2 3 ... n.

Make sure the combinations are sorted.

To elaborate,

    Within every entry, elements should be sorted. [1, 4] is a valid entry while [4, 1] is not.
    Entries should be sorted within themselves.

Example : If n = 4 and k = 2, a solution is:

[
  [1,2],
  [1,3],
  [1,4],
  [2,3],
  [2,4],
  [3,4],
]

'''

class Solution:
	# @param A : integer
	# @param B : integer
	# @return a list of list of integers
	
	def backTrack(self, tmp, arr, start, end, count):
	    if count==0:
	        self.result.append(tmp[:])
	        return
	    if start==end:
	        return
	    
	    for i in range(start, end):
	        tmp.append(arr[i])
	        self.backTrack(tmp, arr, i+1, end, count-1)
	        tmp.pop()
	    
	def combine(self, A, B):
	    
	    self.result = []
	    A = [i for i in range(1, A+1)]
	    self.backTrack([], A, 0, len(A), B)
	    
	    return self.result

