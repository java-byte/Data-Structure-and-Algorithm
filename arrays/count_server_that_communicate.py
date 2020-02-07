

'''

You are given a map of a server center, represented as a m * n integer matrix grid, where 1 means that on that cell there is a server and 0 means that it is no server. Two servers are said to communicate if they are on the same row or on the same column.

Return the number of servers that communicate with any other server.

Input: grid = [[1,0],
	       [0,1]]
Output: 0
Explanation: No servers can communicate with others.


Input: grid = [[1,0],
               [1,1]]
Output: 3
Explanation: All three servers can communicate with at least one other server.


Input: grid = [[1,1,0,0],
	       [0,0,1,0],
               [0,0,1,0],
               [0,0,0,1]]
Output: 4
Explanation: The two servers in the first row can communicate with each other. The two servers in the third column can communicate with each other. The server at right bottom corner can't communicate with any other server.

'''



from collections import defaultdict

class Solution(object):
    def countServers(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        
        row = len(grid)
        if row==0: return 0
        
        col = len(grid[0])
        
        rowCount = defaultdict(int)
        colCount = defaultdict(int)
        
        for i in range(row):
            for j in range(col):
                if grid[i][j]==1:
                    rowCount[i]+=1
                    colCount[j]+=1
        
        count = 0
    
        for i in range(row):
            for j in range(col):
                if grid[i][j]==1 and (rowCount[i]>1 or colCount[j]>1):
                    count+=1
        
        return count



grid = [[1,1,0,0],[0,0,1,0],[0,0,1,0],[0,0,0,1]]
obj = Solution()
print(obj.countServers(grid))



