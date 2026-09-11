# LeetCode #713 - Subarray Product Less Than K
# Difficulty: Medium
# Approach: Sliding Window / Two Pointers
# Time Complexity: O(n)
# Space Complexity: O(1)


class Solution:
    def numSubarrayProductLessThanK(self, nums, k):
        if k <= 1:
            return 0

        left = 0
        product = 1
        count = 0

        for right in range(len(nums)):
            product *= nums[right]

            # Shrink window while product >= k
            while product >= k:
                product //= nums[left]
                left += 1

            # Every subarray ending at right is valid
            count += right - left + 1

        return count


# --------------------------------------------------
# Example
# --------------------------------------------------

nums = [10, 5, 2, 6]
k = 100

solution = Solution()
result = solution.numSubarrayProductLessThanK(nums, k)

print("Input:")
print("nums =", nums)
print("k =", k)

print("\nOutput:")
print(result)