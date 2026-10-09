# LeetCode #424 - Longest Repeating Character Replacement
# Difficulty: Medium
# Approach: Sliding Window / Hashing
# Time Complexity: O(n)
# Space Complexity: O(1)


class Solution:
    def characterReplacement(self, s, k):
        # Frequency of characters in current window
        count = {}

        left = 0
        max_freq = 0
        max_length = 0

        # Expand the window using right pointer
        for right in range(len(s)):

            # Update frequency of current character
            count[s[right]] = count.get(s[right], 0) + 1

            # Maximum frequency in current window
            max_freq = max(max_freq, count[s[right]])

            # Number of characters that need replacement
            replacements = (right - left + 1) - max_freq

            # Shrink window if replacements exceed k
            while replacements > k:
                count[s[left]] -= 1
                left += 1

                replacements = (right - left + 1) - max_freq

            # Update maximum window length
            max_length = max(max_length, right - left + 1)

        return max_length


# --------------------------------------------------
# Example
# --------------------------------------------------

s = "AABABBA"
k = 1

solution = Solution()
result = solution.characterReplacement(s, k)

print("Input:")
print("s =", s)
print("k =", k)

print("\nOutput:")
print(result)