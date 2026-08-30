# LeetCode #121 - Best Time to Buy and Sell Stock
# Difficulty: Easy
# Approach: One Pass
# Time Complexity: O(n)
# Space Complexity: O(1)


class Solution:
    def maxProfit(self, prices):
        min_price = float('inf')
        max_profit = 0

        for price in prices:
            if price < min_price:
                min_price = price

            profit = price - min_price

            if profit > max_profit:
                max_profit = profit

        return max_profit


# --------------------------------------------------
# Example
# --------------------------------------------------

prices = [7, 1, 5, 3, 6, 4]

solution = Solution()
result = solution.maxProfit(prices)

print("Input:")
print("prices =", prices)

print("\nOutput:")
print(result)