# LeetCode #76 - Minimum Window Substring
# Difficulty: Hard
# Approach: Sliding Window / Hashing
# Time Complexity: O(n)
# Space Complexity: O(k)


from collections import Counter


class Solution:
    def minWindow(self, s, t):
        # If t is longer than s, no valid window exists
        if len(t) > len(s):
            return ""

        # Frequency of characters required from t
        required = Counter(t)

        # Current frequency of characters in the window
        window = {}

        # Number of characters whose required frequency is satisfied
        formed = 0
        required_count = len(required)

        # Left pointer of the sliding window
        left = 0

        # Store the smallest window
        min_length = float("inf")
        min_left = 0

        # Expand the window using right pointer
        for right in range(len(s)):

            char = s[right]

            # Add current character to the window
            window[char] = window.get(char, 0) + 1

            # Character requirement is completely satisfied
            if char in required and window[char] == required[char]:
                formed += 1

            # Try shrinking the window
            while formed == required_count and left <= right:

                # Update minimum window
                current_length = right - left + 1

                if current_length < min_length:
                    min_length = current_length
                    min_left = left

                # Remove leftmost character
                left_char = s[left]
                window[left_char] -= 1

                # A required character is no longer satisfied
                if (left_char in required and
                        window[left_char] < required[left_char]):
                    formed -= 1

                # Move left pointer
                left += 1

        # Return the minimum window or empty string
        if min_length == float("inf"):
            return ""

        return s[min_left:min_left + min_length]


# --------------------------------------------------
# Example
# --------------------------------------------------

s = "ADOBECODEBANC"
t = "ABC"

solution = Solution()
result = solution.minWindow(s, t)

print("Input:")
print("s =", s)
print("t =", t)

print("\nOutput:")
print(result)