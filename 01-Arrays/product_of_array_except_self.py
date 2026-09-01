# Product of Array Except Self
# LeetCode: 238
# Approach: Prefix Product + Suffix Product
# Time Complexity: O(n)
# Space Complexity: O(1) - excluding the output array


class solution:
    def productExceptSelf(self, nums):
        n = len(nums)
        result = [1] * n

        # Store prefix products
        for i in range(1, n):
            result[i] = result[i - 1] * nums[i - 1]

        # Multiply with suffix products
        right = 1

        for i in range(n - 1, -1, -1):
            result[i] *= right
            right *= nums[i]

        return result
