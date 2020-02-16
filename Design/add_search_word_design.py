'''

Design a data structure that supports the following two operations:

void addWord(word)
bool search(word)

search(word) can search a literal word or a regular expression string containing only letters a-z or .. A . means it can represent any one letter.

Example:

addWord("bad")
addWord("dad")
addWord("mad")
search("pad") -> false
search("bad") -> true
search(".ad") -> true
search("b..") -> true

Note:
You may assume that all words are consist of lowercase letters a-z.


'''

from collections import defaultdict

class TrieNode:
    def __init__(self):
        self.children = defaultdict(TrieNode)
        self.isLeafNode = False
        
class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()
        

    def addWord(self, word: str) -> None:
        """
        Adds a word into the data structure.
        """
        node = self.root
        
        for w in word:
            node = node.children[w]
        
        node.isLeafNode=True
        
    
    def searchUtil(self, word, index, node):
        
        if index == len(word) and node.isLeafNode:
            return True
        if index==len(word):
            return False
        
        node = node.children
        if word[index]=='.':
            for child in node:
                if self.searchUtil(word, index+1, node[child]):
                    return True
        if word[index] in node:
            return self.searchUtil(word, index+1, node[word[index]])
        else:
            return False
        
    def search(self, word: str) -> bool:
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        """
        parentNode = self.root; n = len(word)
        for i in range(n):
            parentNode = parentNode.children
            if word[i]=='.':
                for child in parentNode:
                    if self.searchUtil(word, i+1, parentNode[child]):
                        return True
            if word[i] in parentNode:
                parentNode = parentNode[word[i]]
            else:
                return False
        
        return parentNode.isLeafNode
    
# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
