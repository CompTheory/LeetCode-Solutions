"""
LeetCode #509 - Fibonacci Number
""" 



# with recusive approach
class Solution:
    def fib(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1:
            return 1
        return self.fib(n - 1) + self.fib(n - 2)

# time complexity = O(2^n)
# time complexity = O(n)




# memoization approach
class Solution:
    def fib(self, n: int) -> int:
        hashmap = dict()
        def memo_fib(n, memo):
            if n == 0:
                return 0
            if n == 1:
                return 1
            if n in memo:
                return memo[n]
            memo[n] = memo_fib(n - 1, memo) + memo_fib(n - 2, memo)
            return memo[n]
        return memo_fib(n, hashmap)

# time complexity = O(n)
# space complexity = O(n)




# Tabulation approach (Bottom-up)
class Solution:
    def fib(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1:
            return 1
        dp = [None] * (n + 1)
        dp[0] = 0
        dp[1] = 1
        if not dp[n]:
            for i in range(2, n + 1):
                dp[i] = dp[i - 1] + dp[i - 2]
        return dp[n]

# time complexity = O(n)
# space complexity = O(n)