# LeetCode #75 - Sort Colors
# Difficulty: Medium
# Approach: Dutch National Flag Algorithm (Three Pointers)
# Time Complexity: O(n)
# Space Complexity: O(1)


class Solution:
    def sortColors(self, nums):
        low = 0
        mid = 0
        high = len(nums) - 1

        while mid <= high:
            if nums[mid] == 0:
                nums[low], nums[mid] = nums[mid], nums[low]
                low += 1
                mid += 1

            elif nums[mid] == 1:
                mid += 1

            else:  # nums[mid] == 2
                nums[mid], nums[high] = nums[high], nums[mid]
                high -= 1


# --------------------------------------------------
# Example
# --------------------------------------------------

nums = [2, 0, 2, 1, 1, 0]

solution = Solution()
solution.sortColors(nums)

print("Input:")
print("Original = [2, 0, 2, 1, 1, 0]")

print("\nOutput:")
print(nums)