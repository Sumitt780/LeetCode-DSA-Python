# LeetCode #10 - Regular Expression Matching
# Difficulty: Hard
# Approach: Dynamic Programming
# Time Complexity: O(m * n)
# Space Complexity: O(m * n)


class Solution:
    def isMatch(self, s, p):
        m = len(s)
        n = len(p)

        # dp[i][j] = True if s[i:] matches p[j:]
        dp = [[False] * (n + 1) for _ in range(m + 1)]

        # Empty string matches empty pattern
        dp[m][n] = True

        # Fill the DP table from bottom-right
        for i in range(m, -1, -1):
            for j in range(n - 1, -1, -1):

                # Check if current characters match
                first_match = (
                    i < m and
                    (s[i] == p[j] or p[j] == ".")
                )

                # Handle '*' wildcard
                if j + 1 < n and p[j + 1] == "*":

                    # '*' matches zero occurrences
                    dp[i][j] = dp[i][j + 2]

                    # '*' matches one or more occurrences
                    if first_match:
                        dp[i][j] = dp[i][j] or dp[i + 1][j]

                else:
                    # Normal character match
                    if first_match:
                        dp[i][j] = dp[i + 1][j + 1]

        return dp[0][0]


# --------------------------------------------------
# Example
# --------------------------------------------------

s = "aab"
p = "c*a*b"

solution = Solution()
result = solution.isMatch(s, p)

print("Input:")
print("s =", s)
print("p =", p)

print("\nOutput:")
print(result)