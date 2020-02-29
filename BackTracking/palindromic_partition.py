'''
Palindrome Partitioning

Problem Description

Given a string s, partition s such that every string of the partition is a palindrome.

Return all possible palindrome partitioning of s.

Ordering the results in the answer : Entry i will come before Entry j if :

    len(Entryi[0]) < len(Entryj[0]) OR
    (len(Entryi[0]) == len(Entryj[0]) AND len(Entryi[1]) < len(Entryj[1])) OR * * *
    (len(Entryi[0]) == len(Entryj[0]) AND ... len(Entryi[k] < len(Entryj[k]))



Problem Constraints

1 <= len(s) <= 15


Input Format
First argument is a string of lowercase characters.


Output Format
Return a list of all possible palindrome partitioning of s.


Example Input

Input 1:

s = "aab"



Example Output

Output 1:

 [
    ["a","a","b"]
    ["aa","b"],
  ]



Example Explanation

Explanation 1:

In the given example, ["a", "a", "b"] comes before ["aa", "b"] because len("a") < len("aa").


'''



class Solution:
    # @param A : string
    # @return a list of list of strings
    
    def isPalindrome(self, string):
        left = 0; right = len(string)-1
        
        while left<=right:
            if string[left]!=string[right]:
                return False
            left+=1
            right-=1
        
        return True
    
    
    def backTrack(self, arr, tmp, start, end):
        if start==end:
            self.result.append(tmp[:])
            return
        
        for i in range(start+1, end+1):
            curr_string = arr[start:i]
            
            if self.isPalindrome(curr_string):
                tmp.append(curr_string)
                
                self.backTrack(arr, tmp, i, end)
                
                tmp.pop()
                
    
    
        
    def partition(self, A):
        
        n = len(A)
        if n==1:
            return [A]
        
        self.result = []
        
        self.backTrack(A,[],0, n)
        
        return self.result
        
        
        
        

