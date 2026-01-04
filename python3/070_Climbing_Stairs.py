"""
LeetCode #70 - Climbing Stairs
"""



# with memoization approach
class Solution:
    def climbStairs(self, n: int) -> int:
        hashmap = dict()
        def help_climb(n, memo):
            if n == 1:
                return 1
            if n == 2:
                return 2
            if n in memo:
                return memo[n]
            memo[n] = help_climb(n - 1, memo) + help_climb(n - 2, memo)
            return memo[n]
        return help_climb(n, hashmap)

# time complexity = O(n)
# space complexity = O(n)






# with Tabulation (bottom-up) approach
class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        if n == 2:
            return 2
        dp = [0] * (n + 1)
        dp[0] = dp[1] = 1
        dp[2] = 2

        for i in range(3, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]
        return dp[n]

# time complexity = O(n)
# space complexity = O(n)