# LeetCode #724 - Find Pivot Index
# Difficulty: Easy
# Approach: Prefix Sum
# Time Complexity: O(n)
# Space Complexity: O(1)


class Solution:
    def pivotIndex(self, nums):
        total = sum(nums)
        left = 0

        for i in range(len(nums)):
            if left == total - left - nums[i]:
                return i

            left += nums[i]

        return -1


# --------------------------------------------------
# Example
# --------------------------------------------------

nums = [1, 7, 3, 6, 5, 6]

solution = Solution()
result = solution.pivotIndex(nums)

print("Input:")
print("Original =", nums)

print("\nOutput:")
print(result)