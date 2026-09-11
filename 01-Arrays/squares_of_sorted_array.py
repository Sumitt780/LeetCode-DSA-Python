# LeetCode #977 - Squares of a Sorted Array
# Difficulty: Easy
# Approach: Two Pointers
# Time Complexity: O(n)
# Space Complexity: O(n) for output


class Solution:
    def sortedSquares(self, nums):
        n = len(nums)
        result = [0] * n

        left = 0
        right = n - 1

        # Fill result from largest to smallest
        for i in range(n - 1, -1, -1):
            if abs(nums[left]) > abs(nums[right]):
                result[i] = nums[left] ** 2
                left += 1
            else:
                result[i] = nums[right] ** 2
                right -= 1

        return result


# --------------------------------------------------
# Example
# --------------------------------------------------

nums = [-4, -1, 0, 3, 10]

solution = Solution()
result = solution.sortedSquares(nums)

print("Input:")
print("Original =", nums)

print("\nOutput:")
print(result)