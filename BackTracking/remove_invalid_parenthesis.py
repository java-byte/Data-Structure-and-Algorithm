'''
Remove Invalid Parentheses

Given a string A consisting of lowercase English alphabets and parentheses '(' and '). Remove the minimum number of invalid parentheses in order to make the input string valid.

Return all possible results.

You can return the results in any order.


Input Format

The only argument given is string A.

Output Format

Return all possible strings after removing the minimum number of invalid parentheses.

Constraints

1 <= length of the string <= 20

For Example

Input 1:
    A = ""()())()"
Output 1:
     ["()()()", "(())()"]
     Explanation 1:
        By removing 1 parentheses we can make the string valid.
                1. Remove the parentheses at index 4 then string becomes : "()()()"
                2. Remove the parentheses at index 2 then string becomes : "(())()"



Input 2:
    A = "(a)())()"
Output 2:
    ["(a)()()", "(a())()"]


'''

from collections import deque

class Solution:
    # @param A : string
    # @return a list of strings
    
    def isValid(self, string):
        openCount = 0
        closeCount = 0
        n = len(string)
        for i in range(n):
            if string[i] not in ['(', ')']:
                continue
            
            if string[i]=='(':
                openCount+=1
            elif openCount<=closeCount:
                return False
            elif string[i]==')':
                closeCount+=1
        return openCount==closeCount
        
    def solve(self, A):
        
        queue = deque()
        self.result = []
        queue.append(A)
        usedSet = set(); usedSet.add(A)
        while len(queue)>0:
            
            flag = False
            for i in range(len(queue)):
                #print(len(queue))
                string = queue.popleft()
                
                if self.isValid(string):
                    flag = True
                    if string not in self.result:
                        self.result.append(string)
                
                if flag==False:
                    for i in range(len(string)):
                        if string[i] in ['(', ')']:
                            new_string = string[:i] + string[i+1:]
                            if new_string not in usedSet:
                                queue.append(new_string)
                                usedSet.add(new_string)
            
            if flag:
                return self.result
        

