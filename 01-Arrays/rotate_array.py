# Rotate Array
# LeetCode: 189
# Approach: Array Reversal
# Time Complexity: O(n)
# Space Complexity: O(1)

# Example:
# Input:  nums = [1, 2, 3, 4, 5, 6, 7], k = 3
# Output: [5, 6, 7, 1, 2, 3, 4]

class Solution:
    def rotate(self, nums, k):
        n = len(nums)
        k = k % n

        def reverse(l, r):
            while l < r:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
                r -= 1

        reverse(0, n - 1)
        reverse(0, k - 1)
        reverse(k, n - 1)