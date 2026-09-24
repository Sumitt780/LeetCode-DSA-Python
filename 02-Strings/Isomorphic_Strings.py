# LeetCode #205 - Isomorphic Strings
# Difficulty: Easy
# Approach: Hashing / Two Hash Maps
# Time Complexity: O(n)
# Space Complexity: O(n)


class Solution:
    def isIsomorphic(self, s, t):
        # Two dictionaries to maintain character mappings
        s_to_t = {}
        t_to_s = {}

        # Traverse both strings simultaneously
        for i in range(len(s)):

            char_s = s[i]
            char_t = t[i]

            # Check mapping from s -> t
            if char_s in s_to_t:
                if s_to_t[char_s] != char_t:
                    return False

            # Check mapping from t -> s
            if char_t in t_to_s:
                if t_to_s[char_t] != char_s:
                    return False

            # Create the mappings
            s_to_t[char_s] = char_t
            t_to_s[char_t] = char_s

        return True


# --------------------------------------------------
# Example
# --------------------------------------------------

s = "egg"
t = "add"

solution = Solution()
result = solution.isIsomorphic(s, t)

print("Input:")
print("s =", s)
print("t =", t)

print("\nOutput:")
print(result)