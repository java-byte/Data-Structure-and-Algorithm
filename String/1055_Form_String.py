'''
From any string, we can form a subsequence of that string by deleting some number of characters (possibly no deletions).

Given two strings source and target, return the minimum number of subsequences of source such that their concatenation equals target. If the task is impossible, return -1.

 

Example 1:

Input: source = "abc", target = "abcbc"
Output: 2
Explanation: The target "abcbc" can be formed by "abc" and "bc", which are subsequences of source "abc".

Example 2:

Input: source = "abc", target = "acdbc"
Output: -1
Explanation: The target string cannot be constructed from the subsequences of source string due to the character "d" in target string.

Example 3:

Input: source = "xyz", target = "xzyxz"
Output: 3
Explanation: The target string can be constructed as follows "xz" + "y" + "xz".

 

Constraints:

    Both the source and target strings consist of only lowercase English letters from "a"-"z".
    The lengths of source and target string are between 1 and 1000.


'''

from collections import Counter, defaultdict

class Solution:
    
    def isSubsequence(self, text, pattern):
        row, col = len(pattern), len(text)
        dp = [[False for i in range(col+1)] for j in range(row+1)]
        
        for i in range(col+1):
            dp[0][i] = True
        for i in range(1, row+1):
            for j in range(1, col+1):
                if pattern[i-1]==text[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = dp[i][j-1]
        
        return dp[-1][-1]
    
    
    def binarySearch(self, arr, target):
        
        start = 0; end = len(arr) -1; candidate=None
        
        while start<=end:
            mid = start + (end-start)//2
            
            if arr[mid]>target:
                candidate = arr[mid]
                end = mid -1
            else:
                start = mid + 1
        
        return candidate if candidate!=None else -1
            
            
    def shortestWay(self, source: str, target: str) -> int:
    
        count = 0; t_len = len(target)
        if t_len==0: return 0
        
        #keysDict = Counter(source)
        
        '''
        Method-1: Brute force with DP- TLE 
        start = 0; end=1
        while end<=n:
            if target[end-1] not in keysDict:
                return -1
            if not self.isSubsequence(source, target[start:end]):
                count +=1
                start = end-1
            end+=1
        return count
        
        '''
        
        '''
        Method-2: Without DP
        
        Time complexity = O(M*N), Space = O(M)
        
        i = 0
        while i<n:
            if target[i] not in keysDict:
                return -1
            for j in range(len(source)):
                if i<n and source[j]==target[i]:
                    i+=1
            if i<n:
                count+=1
        return count
                
        '''
        
        '''
        Method-2: Binary Search based approach
        '''
        
        s_len = len(source)
        source_dict = defaultdict(list)
        
        for i in range(s_len):
            source_dict[source[i]].append(i)
        
        targetIndex = 0;
        
        while targetIndex < t_len:
            if targetIndex==t_len:
                break
                
            sourceIndex = 0; count+=1
            while sourceIndex < s_len:
                if targetIndex < t_len and target[targetIndex] not in source_dict:
                    return -1
                if targetIndex < t_len and target[targetIndex] == source[sourceIndex]:
                    targetIndex+=1
                    sourceIndex+=1
                elif targetIndex < t_len and target[targetIndex] != source[sourceIndex]:
                    indexArray = source_dict[target[targetIndex]]
                    
                    index = self.binarySearch(indexArray, sourceIndex)
                    
                    if index==-1:
                        break
                    else:
                        targetIndex+=1
                        sourceIndex = index+1
                #print(sourceIndex, targetIndex)
                if sourceIndex==s_len:
                    break
                if targetIndex==t_len:
                    break
                
        
        return count
                
                
                
        
        
                
                
                
            
