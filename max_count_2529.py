import bisect
from typing import List

class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        first_positive = bisect.bisect_left(nums, 1)
        print("First positive index:", first_positive)
        first_negative = bisect.bisect_right(nums, -1)
        print("First negative index:", first_negative)

        neg_count = last_negative
        pos_count = len(nums) - first_positive
        return max(neg_count, pos_count)

solution = Solution()
solution.maximumCount([-3, -2, -1, 0, 0, 1, 2, 3])
