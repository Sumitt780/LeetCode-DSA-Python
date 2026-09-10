# LeetCode #53 - Maximum Subarray
# Difficulty: Medium
# Approach: Kadane's Algorithm
# Time Complexity: O(n)
# Space Complexity: O(1)


class Solution:
    def maxSubArray(self, nums):
        maxSum = nums[0]
        currentSum = 0

        for i in range(len(nums)):
            currentSum += nums[i]

            if currentSum > maxSum:
                maxSum = currentSum

            if currentSum < 0:
                currentSum = 0

        return maxSum


# --------------------------------------------------
# Example
# --------------------------------------------------

nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]

solution = Solution()
result = solution.maxSubArray(nums)

print("Input:")
print("Original =", nums)

print("\nOutput:")
print(result)