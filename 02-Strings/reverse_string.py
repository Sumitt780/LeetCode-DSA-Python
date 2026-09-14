# LeetCode #344 - Reverse String
# Difficulty: Easy
# Approach: Two Pointers
# Time Complexity: O(n)
# Space Complexity: O(1)


class Solution:
    def reverseString(self, s):
        # Use two pointers from both ends
        left = 0
        right = len(s) - 1

        while left < right:

            # Swap elements
            s[left], s[right] = s[right], s[left]

            # Move pointers towards the center
            left += 1
            right -= 1


# --------------------------------------------------
# Example
# --------------------------------------------------

s = ["h", "e", "l", "l", "o"]

solution = Solution()
solution.reverseString(s)

print("Input:")
print(["h", "e", "l", "l", "o"])

print("\nOutput:")
print(s)