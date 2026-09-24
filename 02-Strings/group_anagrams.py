# LeetCode #49 - Group Anagrams
# Difficulty: Medium
# Approach: Hashing / Sorting
# Time Complexity: O(n * k log k)
# Space Complexity: O(n * k)


class Solution:
    def groupAnagrams(self, strs):
        # Dictionary to store anagrams
        anagrams = {}

        # Traverse each word
        for word in strs:

            # Sort characters to create a common key
            key = ''.join(sorted(word))

            # Add word to the corresponding group
            if key not in anagrams:
                anagrams[key] = []

            anagrams[key].append(word)

        # Return all grouped anagrams
        return list(anagrams.values())


# --------------------------------------------------
# Example
# --------------------------------------------------

strs = ["eat", "tea", "tan", "ate", "nat", "bat"]

solution = Solution()
result = solution.groupAnagrams(strs)

print("Input:")
print("strs =", strs)

print("\nOutput:")
print(result)