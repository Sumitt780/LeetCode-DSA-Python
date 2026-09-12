# LeetCode #525 - Contiguous Array
# Difficulty: Medium
# Approach: Prefix Sum + Hash Map
# Time Complexity: O(n)
# Space Complexity: O(n)


class Solution:
    def findMaxLength(self, nums):
        count = 0
        max_length = 0

        # Store first index where each count occurs
        first_index = {0: -1}

        for i in range(len(nums)):
            # Treat 0 as -1 and 1 as +1
            if nums[i] == 0:
                count -= 1
            else:
                count += 1

            # Same count means equal number of 0s and 1s
            if count in first_index:
                max_length = max(max_length, i - first_index[count])
            else:
                first_index[count] = i

        return max_length


# --------------------------------------------------
# Example
# --------------------------------------------------

nums = [0, 1, 0]

solution = Solution()
result = solution.findMaxLength(nums)

print("Input:")
print("nums =", nums)

print("\nOutput:")
print(result)