# LeetCode #5 - Longest Palindromic Substring
# Difficulty: Medium
# Approach: Expand Around Center
# Time Complexity: O(n^2)
# Space Complexity: O(1)


class Solution:
    def longestPalindrome(self, s):
        # If string is empty or has only one character
        if len(s) < 2:
            return s

        start = 0
        end = 0

        # Expand around every possible center
        for i in range(len(s)):

            # Odd length palindrome
            left1, right1 = self.expandAroundCenter(s, i, i)

            # Even length palindrome
            left2, right2 = self.expandAroundCenter(s, i, i + 1)

            # Choose the longer palindrome
            if right1 - left1 > end - start:
                start = left1
                end = right1

            if right2 - left2 > end - start:
                start = left2
                end = right2

        return s[start:end + 1]

    def expandAroundCenter(self, s, left, right):
        # Expand while characters are equal
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1

        # Return valid palindrome boundaries
        return left + 1, right - 1


# --------------------------------------------------
# Example
# --------------------------------------------------

s = "babad"

solution = Solution()
result = solution.longestPalindrome(s)

print("Input:")
print("s =", s)

print("\nOutput:")
print(result)