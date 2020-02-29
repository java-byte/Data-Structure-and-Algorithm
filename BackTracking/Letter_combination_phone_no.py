'''

Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent.

A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.

Input: "23"
Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].

Note:

Although the above answer is in lexicographical order, your answer could be in any order you want.

'''

class Solution:
    
    def FindCombination(self, index, mapDict, digits, currString):
        if index==len(digits)-1:
            num = int(digits[index])
            for value in mapDict[num]:
                self.result.append("".join(currString + [value]))
        else:
            num = int(digits[index])
            for value in mapDict[num]:
                self.FindCombination(index+1, mapDict, digits, currString+[value])
                
    def letterCombinations(self, digits: str) -> List[str]:
        
        mappingDict = {
                       2:['a','b','c'],
                       3:['d','e','f'],
                       4:['g','h','i'],
                       5:['j','k','l'],
                       6:['m','n','o'],
                       7:['p','q','r','s'],
                       8:['t','u','v'],
                       9:['w','x','y','z']
                      }
        
        self.result = []
        n = len(digits)
        if n==0:
            return self.result
        #self.FindCombination(0,mappingDict,digits,[])  ## Recursive Method
        #return self.result
        
        output = set()
        output.add("")
        
        ## Iterative method
        ## Time Complexity - O(4^n)
        for item in digits:
            output = {ch+val for ch in output for val in mappingDict[int(item)]}
                
        return output
        


