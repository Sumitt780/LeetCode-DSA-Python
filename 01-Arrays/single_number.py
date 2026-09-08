# LeetCode #136 - Single Number
# Difficulty: Easy
# Approach: XOR
# Time Complexity: O(n)
# Space Complexity: O(1)


class Solution:
    def singleNumber(self, nums):
        res = 0

        for n in nums:
            res ^= n

        return res


# --------------------------------------------------
# Example
# --------------------------------------------------

nums = [4, 1, 2, 1, 2]

solution = Solution()
result = solution.singleNumber(nums)

print("Input:")
print("nums =", nums)

print("\nOutput:")
print(result)