'''
SIXLETS

Given a array of integers A of size N and an integer B.

Return number of non-empty subsequences of A of size B having sum <= 1000.
Input Format

The first argument given is the integer array A.
The second argument given is the integer B.

Output Format

Return number of subsequences of A of size B having sum <= 1000.

Constraints

1 <= N <= 20
1 <= A[i] <= 1000
1 <= B <= N

For Example

Input 1:
    A = [1, 2, 8]
    B = 2
Output 1:
    3
Explaination 1:
    {1, 2}, {1, 8}, {2, 8}

Input 2:
    A = [5, 17, 1000, 11]
    B = 4
Output 2:
    0


'''

class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    
    def backTrack(self, arr, curr_len, curr_sum, start, end):
        if curr_len==self.target:
            if curr_sum<=1000:
                self.result+=1
        if start==end or curr_sum>=1000:
            return
        
        for i in range(start, end):
            if curr_sum+arr[i]<=1000:
                curr_sum += arr[i]
                curr_len += 1
                self.backTrack(arr, curr_len, curr_sum, i+1, end)
                curr_sum -= arr[i]
                curr_len -=1
                
        
    def solve(self, A, B):
        
        self.result = 0
        n = len(A); self.target=B
        self.backTrack(A,0,0,0,n)
        
        return self.result

