class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        r = len(numbers)-1
        l = 0
        while(l < r):
            sum = numbers[l] + numbers[r]
            if (sum == target):
                return [l+1, r+1]
            elif(sum < target):
                l = l+1
            else:
                r = r-1