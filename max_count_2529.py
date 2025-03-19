import bisect
from typing import List

class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        n = len(nums)
        
        # Binary search for the first positive number (> 0)
        lo, hi = 0, n
        while lo < hi:
            mid = (lo + hi) // 2
            if nums[mid] > 0:
                hi = mid
            else:
                lo = mid + 1
        pos_count = n - lo

        # Binary search for the first non-negative number (>= 0)
        lo, hi = 0, n
        while lo < hi:
            mid = (lo + hi) // 2
            if nums[mid] < 0:
                lo = mid + 1
            else:
                hi = mid
        neg_count = lo

        return max(pos_count, neg_count)


solution = Solution()
solution.maximumCount([-3, -2, -1, 0, 0, 1, 2, 3])
