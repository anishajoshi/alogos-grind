# Top K Frequent Elements
from collections import defaultdict
import heapq
from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numsMap = defaultdict(int)
        for num in nums:
            numsMap[num] += 1
        
        minHeap = []
        for element, freq in numsMap.items():
            heapq.heappush(minHeap, (freq, element))
            if (len(minHeap) > k):
                heapq.heappop(minHeap)
        result = []
        for freq, num in minHeap:
            result.append(num)

        return result


solution = Solution()
print(solution.topKFrequent([1,2,2,3,3,3,4,4,4,4,4], 2))