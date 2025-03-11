# Valid Palindrome

class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned_str = ""
        for char in s:
            if char.isalnum():
                cleaned_str += char
        cleaned_str = cleaned_str.lower()
        reversed_str = cleaned_str[::-1]
        if cleaned_str == reversed_str:
            return True
        return False

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
