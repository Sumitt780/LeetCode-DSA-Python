# LeetCode #128 - Longest Consecutive Sequence
# Difficulty: Medium
# Approach: Hash Set
# Time Complexity: O(n)
# Space Complexity: O(n)


class Solution:
    def longestConsecutive(self, nums):
        num_set = set(nums)
        longest = 0

        for num in num_set:
            # Start only if num is the beginning of a sequence
            if num - 1 not in num_set:
                current = num
                length = 1

                while current + 1 in num_set:
                    current += 1
                    length += 1

                longest = max(longest, length)

        return longest


# --------------------------------------------------
# Example
# --------------------------------------------------

nums = [100, 4, 200, 1, 3, 2]

solution = Solution()
result = solution.longestConsecutive(nums)

print("Input:")
print("nums =", nums)

print("\nOutput:")
print(result)