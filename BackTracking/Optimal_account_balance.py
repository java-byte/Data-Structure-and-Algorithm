'''
A group of friends went on holiday and sometimes lent each other money. For example, Alice paid for Bill's lunch for $10. Then later Chris gave Alice $5 for a taxi ride. We can model each transaction as a tuple (x, y, z) which means person x gave person y $z. Assuming Alice, Bill, and Chris are person 0, 1, and 2 respectively (0, 1, 2 are the person's ID), the transactions can be represented as [[0, 1, 10], [2, 0, 5]].

Given a list of transactions between a group of people, return the minimum number of transactions required to settle the debt.

Note:

    A transaction will be given as a tuple (x, y, z). Note that x ≠ y and z > 0.
    Person's IDs may not be linear, e.g. we could have the persons 0, 1, 2 or we could also have the persons 0, 2, 6.

Example 1:

Input:
[[0,1,10], [2,0,5]]

Output:
2

Explanation:
Person #0 gave person #1 $10.
Person #2 gave person #0 $5.

Two transactions are needed. One way to settle the debt is person #1 pays person #0 and #2 $5 each.

Example 2:

Input:
[[0,1,10], [1,0,1], [1,2,5], [2,0,5]]

Output:
1

Explanation:
Person #0 gave person #1 $10.
Person #1 gave person #0 $1.
Person #1 gave person #2 $5.
Person #2 gave person #0 $5.

Therefore, person #1 only need to give person #0 $4, and all debt is settled.

'''

from collections import defaultdict
class Solution:
    
    def DFS(self, startIndex, n):
        while startIndex<n and self.non_zero[startIndex]==0:
            startIndex+=1
        if startIndex==n: return 0
        
        minTransaction = float('inf')
        
        for i in range(startIndex+1, n):
            if self.non_zero[startIndex]*self.non_zero[i]<0:
                self.non_zero[i] += self.non_zero[startIndex]
                minTransaction = min(minTransaction, 1 + self.DFS(startIndex+1, n))
                self.non_zero[i] -= self.non_zero[startIndex]
                
        return minTransaction
    
    def minTransfers(self, transactions: List[List[int]]) -> int:
        
        graph = defaultdict(int)
        
        for t in transactions:
            From, To, Rupee = t[0], t[1], t[2]
            graph[From]+=Rupee
            graph[To]-=Rupee
        
        #print(graph)
        self.non_zero = []
        for key, value in graph.items():
            if value!=0:
                self.non_zero.append(value)
               
        ## Till now we have all non-zero value. now we have to find most optimal way of settling it, means which requires less no. of transaction.
        
        ## Our Approach will exhaustive search to try all the combination to find the minimum transaction. Greedy approach will not work here.
        
        return self.DFS(0, len(self.non_zero))
        
