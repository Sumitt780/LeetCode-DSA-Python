# LeetCode #283 - Move Zeroes
# Difficulty: Easy
# Approach: Two Pointers
# Time Complexity: O(n)
# Space Complexity: O(1)


class Solution:
    def moveZeroes(self, nums):
        left = 0

        for right in range(len(nums)):
            if nums[right] != 0:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1


# --------------------------------------------------
# Example
# --------------------------------------------------

nums = [0, 1, 0, 3, 12]

solution = Solution()
solution.moveZeroes(nums)

print("Input:")
print("Original = [0, 1, 0, 3, 12]")

print("\nOutput:")
print(nums)