'''

All Unique Permutations

Given a collection of numbers that might contain duplicates, return all possible unique permutations.

Example : [1,1,2] have the following unique permutations:

[1,1,2]
[1,2,1]
[2,1,1]



'''

class Solution:
	# @param A : list of integers
	# @return a list of list of integers
	
	def backTrack(self, arr, start, end):
	    if start==end:
	        self.result.append(arr[:])
	        return
	    for i in range(start, end):
	        flag=True
	        for k in range(start, i):
	            if arr[k]==arr[i]:
	                flag=False
	                break
	        if flag:
	            arr[i], arr[start] = arr[start], arr[i]
	            self.backTrack(arr, start+1, end)
	            arr[i], arr[start] = arr[start], arr[i]
	            
	def permute(self, A):
	    n = len(A)
	    self.result = []
	    start =0; end = n
	    
	    self.backTrack(A, start, end)
	    
	    return self.result

