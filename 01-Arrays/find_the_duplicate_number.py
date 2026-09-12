# LeetCode #287 - Find the Duplicate Number
# Difficulty: Medium
# Approach: Floyd's Cycle Detection (Tortoise and Hare)
# Time Complexity: O(n)
# Space Complexity: O(1)


class Solution:
    def findDuplicate(self, nums):
        # Phase 1: Find intersection point
        slow = nums[0]
        fast = nums[0]

        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]

            if slow == fast:
                break

        # Phase 2: Find entrance of the cycle
        slow = nums[0]

        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]

        return slow


# --------------------------------------------------
# Example
# --------------------------------------------------

nums = [1, 3, 4, 2, 2]

solution = Solution()
result = solution.findDuplicate(nums)

print("Input:")
print("nums =", nums)

print("\nOutput:")
print(result)