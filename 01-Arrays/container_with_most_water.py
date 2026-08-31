# Container With Most Water
# LeetCode: 11
# Approach: Two Pointers
# Time Complexity: O(n)
# Space Complexity: O(1)

class Solution:
    def maxArea(self, height):
        left = 0
        right = len(height) - 1
        max_water = 0

        while left < right:
            width = right - left
            h = min(height[left], height[right])
            area = width * h

            max_water = max(max_water, area)

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return max_water