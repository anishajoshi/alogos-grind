# Valid Palindrome - Easy . Two pointers

class Solution:
    def isPalindrome(self, s: str) -> bool:
        l = 0
        r = len(s) - 1

        while l < r:
            while l < r and not s[l].isalnum():
                l += 1
            while l < r and not s[r].isalnum():
                r -= 1
            if s[l].lower() != s[r].lower():
                return False
            l+= 1
            r -= 1
        return True
        

   
        '''
        while L < R:
         if s[L] == s[R]:
           L += 1
           R -= 1
         else:
          return False
        '''
        
        
        '''
        cleaned_str = ""
        for char in s:
            if char.isalnum():
                cleaned_str += char
        cleaned_str = cleaned_str.lower()
        reversed_str = cleaned_str[::-1]
        if cleaned_str == reversed_str:
            return True
        return False
    '''

def test():
    solution = Solution()
    
    test_cases = [
        ("Was it a car or a cat I saw?", True),
        ("tab a cat", False),
        ("racecar", True),
        ("A man, a plan, a canal: Panama", True),
        (" ", True),
        ("0P", False)
    ]
    
    for i, (input_str, expected) in enumerate(test_cases):
        result = solution.isPalindrome(input_str)
        print(f"real: {result} exp: {expected}")

# Run tests
if __name__ == "__main__":
    test()
