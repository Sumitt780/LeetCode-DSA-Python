# LeetCode #3 - Longest Substring Without Repeating Characters
# Difficulty: Medium
# Approach: Sliding Window + Hash Map
# Time Complexity: O(n)
# Space Complexity: O(min(n, charset))


class Solution:
    def lengthOfLongestSubstring(self, s):
        # Store the latest index of each character
        last_seen = {}

        left = 0
        max_length = 0

        for right in range(len(s)):

            # If character is already inside the window,
            # move the left pointer
            if s[right] in last_seen:
                left = max(left, last_seen[s[right]] + 1)

            # Update the character's latest index
            last_seen[s[right]] = right

            # Calculate current window length
            max_length = max(max_length, right - left + 1)

        return max_length


# --------------------------------------------------
# Example
# --------------------------------------------------

s = "abcabcbb"

solution = Solution()
result = solution.lengthOfLongestSubstring(s)

print("Input:")
print("s =", s)

print("\nOutput:")
print(result)