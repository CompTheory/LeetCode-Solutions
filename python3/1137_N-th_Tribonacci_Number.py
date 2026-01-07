"""
LeetCode #1137 - N-th Tribonacci Number
"""



# recursive approach
class Solution:
    def tribonacci(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1:
            return 1
        if n == 2:
            return 1
        return self.tribonacci(n - 1) + self.tribonacci(n - 2) + self.tribonacci(n - 3)

# time complexity = O(3^n)
# space complexity = O(n)




# memoization approach
class Solution:
    def tribonacci(self, n: int) -> int:
        memo = dict()
        return self.memo_tribonacci(n, memo)

    def memo_tribonacci(self, n, memo):
        if n in memo:
            return memo[n]
        if n == 0:
            return 0
        if n == 1:
            return 1
        if n == 2:
            return 1
        q = self.memo_tribonacci(n - 1, memo) + self.memo_tribonacci(n - 2, memo) + self.memo_tribonacci(n - 3, memo)
        memo[n] = q
        return memo[n]
    
# time complexity = O(n)
# space complexity = O(n)
    



# tabulation approach (bottom-up)
class Solution:
    def tribonacci(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1:
            return 1
        if n == 2:
            return 1
        dp = [None] * (n + 1)
        dp[0] = 0
        dp[1] = 1
        dp[2] = 1
        for i in range(3, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3]
        return dp[n] 

# time complexity = O(n)
# space complexity = O(n)