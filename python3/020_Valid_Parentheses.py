"""
LeetCode #20 - Valid Parentheses
Youtube Video: https://www.youtube.com/watch?v=_MSzYuzGydk&t=4s
"""


class Solution:
    def isValid(self, s: str) -> bool:
        hashmap = {")" : "(", "}" : "{", "]" : "["}
        stack = []

        for var in s:
            if var not in hashmap:
                stack.append(var)
            else:
                if not stack:
                    return False
                last = stack.pop()
                if last != hashmap[var]:
                    return False

        return not stack


# time complexity = O(n)
# space complexity = O(n)


# # Example Usage:
# Input: s = "()[]{}"
# Output: true
