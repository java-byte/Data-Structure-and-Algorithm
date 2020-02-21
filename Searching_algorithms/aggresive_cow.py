'''
Aggressive cows

Problem Description
Farmer John has built a new long barn, with N stalls. Given an array of integers A of size N where each element of the array represents the location of the stall, and an integer B which represent the number of cows.

His cows don't like this barn layout and become aggressive towards each other once put into a stall. To prevent the cows from hurting each other, John wants to assign the cows to the stalls, such that the minimum distance between any two of them is as large as possible. What is the largest minimum distance?



Problem Constraints

2 <= N <= 100000
0 <= A[i] <= 10^9
2 <= B <= N


Input Format

The first argument given is the integer array A.
The second argument given is the integer B.


Output Format

Return the largest minimum distance possible among the cows.


Example Input

A = [1, 2, 3, 4, 5]
B = 3


Example Output

2


Example Explanation

John can assign the stalls at location 1,3 and 5 to the 3 cows respectively.
So the minimum distance will be 2.


'''


class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        A.sort()
        n = len(A)
        left = 0
        right = A[-1] - A[0]
        
        while left<=right:
            mid = left + (right - left)//2
            
            prev = A[0];cow=1
            for i in range(1, n):
                diff = A[i] - prev
                if diff>=mid:
                    prev = A[i]
                    cow += 1
            if cow>=B:  ## Because we want to maximize the distance.
                left = mid + 1
            else:
                right = mid - 1
        
        return right
