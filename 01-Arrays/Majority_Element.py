# LeetCode #1 - Two Sum
# Difficulty: Easy
# Approach: Hash Map
# Time Complexity: O(n)
# Space Complexity: O(n)


class Solution:
    def twoSum(self, nums, target):
        seen = {}

        for i, num in enumerate(nums):
            complement = target - num

            if complement in seen:
                return [seen[complement], i]

            seen[num] = i


# --------------------------------------------------
# Example
# --------------------------------------------------

nums = [2, 7, 11, 15]
target = 9

solution = Solution()
result = solution.twoSum(nums, target)

print("Input:")
print("nums =", nums)
print("target =", target)

print("\nOutput:")
print(result)