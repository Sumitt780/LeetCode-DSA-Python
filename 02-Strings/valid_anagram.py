# LeetCode #242 - Valid Anagram
# Difficulty: Easy
# Approach: Hashing / Frequency Count
# Time Complexity: O(n)
# Space Complexity: O(n)


from collections import Counter


class Solution:
    def isAnagram(self, s, t):
        # If lengths are different, they cannot be anagrams
        if len(s) != len(t):
            return False

        # Count frequency of characters in both strings
        s_count = Counter(s)
        t_count = Counter(t)

        # Compare both frequency maps
        return s_count == t_count


# --------------------------------------------------
# Example
# --------------------------------------------------

s = "anagram"
t = "nagaram"

solution = Solution()
result = solution.isAnagram(s, t)

print("Input:")
print("s =", s)
print("t =", t)

print("\nOutput:")
print(result)