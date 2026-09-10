# LeetCode #15 - 3Sum
# Difficulty: Medium
# Approach: Sorting + Two Pointers
# Time Complexity: O(n^2)
# Space Complexity: O(1) excluding output


class Solution:
    def threeSum(self, nums):
        nums.sort()
        result = []

        for i in range(len(nums)):
            # Skip duplicates
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            left = i + 1
            right = len(nums) - 1

            while left < right:
                total = nums[i] + nums[left] + nums[right]

                if total == 0:
                    result.append([nums[i], nums[left], nums[right]])

                    # Skip duplicates
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1

                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1

                    left += 1
                    right -= 1

                elif total < 0:
                    left += 1

                else:
                    right -= 1

        return result


# --------------------------------------------------
# Example
# --------------------------------------------------

nums = [-1, 0, 1, 2, -1, -4]

solution = Solution()
result = solution.threeSum(nums)

print("Input:")
print("Original = [-1, 0, 1, 2, -1, -4]")

print("\nOutput:")
print(result)