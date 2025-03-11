from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_map = {}  # Dictionary to store {value: index}
        # Iterate through the list while keeping track of both index (i) and value (num)
        for i, num in enumerate(nums):
            search = target - num  # Calculate the required complement
            # If the complement is already in num_map, return its index and current index
            if search in num_map:
                return [num_map[search], i]  # Found the solution
            # Store the current number with its index in the dictionary
            num_map[num] = i  
