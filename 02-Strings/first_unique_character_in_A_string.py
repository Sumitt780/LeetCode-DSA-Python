# LeetCode #387 - First Unique Character in a String
# Difficulty: Easy
# Approach: Hashing / Frequency Count
# Time Complexity: O(n)
# Space Complexity: O(n)


from collections import Counter


class Solution:
    def firstUniqChar(self, s):
        # Count frequency of every character
        char_count = Counter(s)

        # Find the first character with frequency 1
        for i, char in enumerate(s):
            if char_count[char] == 1:
                return i

        # No unique character found
        return -1


# --------------------------------------------------
# Example
# --------------------------------------------------

s = "leetcode"

solution = Solution()
result = solution.firstUniqChar(s)

print("Input:")
print("s =", s)

print("\nOutput:")
print(result)