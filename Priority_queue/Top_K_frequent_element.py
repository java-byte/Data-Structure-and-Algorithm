'''

Given a non-empty array of integers, return the k most frequent elements.

Example 1:

Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]

Example 2:

Input: nums = [1], k = 1
Output: [1]

Note:

    You may assume k is always valid, 1 ≤ k ≤ number of unique elements.
    Your algorithm's time complexity must be better than O(n log n), where n is the array's size.


'''

import heapq
from collections import Counter
class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        
        ## Total time complexity - O(Nlogk)
        ## Space complexity - O(k)+O(N) - to maintain heap and counter 
        n = len(nums)
        
        pq = []
        
        counter = Counter(nums) # O(N)
        
        for key, value in counter.items(): # O(Nlogk)
            if len(pq)<k:
                heapq.heappush(pq, [value, key])
            else:
                if pq[0][0]<value:
                    pq[0] = [value, key]
                    heapq.heapify(pq)
        
        output = []
        for item in pq:
            output.append(item[1])
        return output
