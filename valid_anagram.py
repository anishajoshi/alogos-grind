class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False  # Quick length check

        # Approach 1: Using Two Dictionaries
        s_dict = {}
        t_dict = {}

        for i in s:
            s_dict[i] = s_dict.get(i, 0) + 1
        for j in t:
            t_dict[j] = t_dict.get(j, 0) + 1

        if s_dict == t_dict:
            return True

        # Approach 2: Using One Dictionary (More Efficient)
        char_count = {}

        for i in range(len(s)):  
            char_count[s[i]] = char_count.get(s[i], 0) + 1  # Increment for s
            char_count[t[i]] = char_count.get(t[i], 0) - 1  # Decrement for t

        for value in char_count.values():
            if value != 0:
                return False  # If any count is non-zero, it's NOT an anagram
        return True  # If all counts are zero, it's an anagram
