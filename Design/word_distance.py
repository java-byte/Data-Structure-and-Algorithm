'''
Design a class which receives a list of words in the constructor, and implements a method that takes two words word1 and word2 and return the shortest distance between these two words in the list. Your method will be called repeatedly many times with different parameters. 

Example:
Assume that words = ["practice", "makes", "perfect", "coding", "makes"].

Input: word1 = “coding”, word2 = “practice”
Output: 3

Input: word1 = "makes", word2 = "coding"
Output: 1

Note:
You may assume that word1 does not equal to word2, and word1 and word2 are both in the list.


'''

from collections import defaultdict

class WordDistance:

    def __init__(self, words: List[str]):
        
        self.wordDict = defaultdict(list)
        for index, value in enumerate(words):
            self.wordDict[value].append(index)
        
    def shortest(self, word1: str, word2: str) -> int:
       
        word1Index = self.wordDict[word1]
        word2Index = self.wordDict[word2]
        
        minDist = float('inf')
        
        '''
        Binary Search based Approach - Complexity - O(nlogn)
        for index in word1Index:
            dist = self.binarySearch(word2Index, index)
            minDist = min(minDist, dist)
        
        self.cache[(word1,word2)] = minDist
        
        return minDist
        '''
        
        ## Method - 2: O(m+n) time complexity
        index1=0; index2=0
        while index1<len(word1Index) and index2<len(word2Index):
            minDist = min(minDist, abs(word1Index[index1] - word2Index[index2]))
            if word1Index[index1]<word2Index[index2]:
                index1+=1
            else:
                index2+=1
        
        return minDist
    
    
    '''
    def binarySearch(self, arr, target):
        n = len(arr)
        start = 0; end = n-1
        
        candidate = float('inf')
        while start<=end:
            mid = start + (end - start)//2
            
            candidate = min(candidate, abs(target - arr[mid]))
            if arr[mid]<target:
                start = mid+1
            else:
                end = mid - 1
        
        return candidate
     '''
    
        
# Your WordDistance object will be instantiated and called as such:
# obj = WordDistance(words)
# param_1 = obj.shortest(word1,word2)
