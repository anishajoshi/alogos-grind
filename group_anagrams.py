# Group Anagrams

from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        myMap = {}
        for i in strs:
            sorted_str = ''.join(sorted(i))
            if sorted_str not in myMap:
                myMap[sorted_str] = []
            myMap[sorted_str].append(i)
        return list((myMap.values()))

solution = Solution()
print(solution.groupAnagrams(["act", "pots", "tops", "cat", "stop", "hat"]))  # Example input
