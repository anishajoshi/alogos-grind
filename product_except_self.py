from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = len(nums) * [1]
        n = len(nums)
        
        left_product = 1
        for i in range(n):
            output[i] = left_product
            left_product *= nums[i]

        right_product = 1
        for i in range(n-1, -1, -1):
            output[i] *= right_product
            right_product *= nums[i]

        return output