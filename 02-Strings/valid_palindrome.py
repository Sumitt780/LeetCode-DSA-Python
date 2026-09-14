# LeetCode #125 - Valid Palindrome
# Difficulty: Easy
# Approach: Two Pointers
# Time Complexity: O(n)
# Space Complexity: O(1)


class Solution:
    def isPalindrome(self, s):
        # Two pointers starting from both ends
        left = 0
        right = len(s) - 1

        while left < right:

            # Skip non-alphanumeric characters
            while left < right and not s[left].isalnum():
                left += 1

            while left < right and not s[right].isalnum():
                right -= 1

            # Compare characters ignoring case
            if s[left].lower() != s[right].lower():
                return False

            # Move both pointers
            left += 1
            right -= 1

        return True


# --------------------------------------------------
# Example
# --------------------------------------------------

s = "A man, a plan, a canal: Panama"

solution = Solution()
result = solution.isPalindrome(s)

print("Input:")
print("s =", s)

print("\nOutput:")
print(result)