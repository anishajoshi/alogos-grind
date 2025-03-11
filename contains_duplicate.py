from typing import List

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        repeat = set()
        for i in range(len(nums)):
            if nums[i] in repeat:
                return True
            else:
                repeat.add(nums[i]) 
        return False         