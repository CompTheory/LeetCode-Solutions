"""
LeetCode #121 - Best Time to Buy and Sell Stock 
"""




# turn into maximum subarray question and using kadane's algorithm
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        diff = []
        len_prices = len(prices)
        for i in range(1, len_prices):
            diff.append(prices[i] - prices[i - 1])
        maximum_profit = float("-inf")
        last_profit = 0
        for p in diff:
            last_profit += p
            if last_profit < 0:
                last_profit = 0
                continue
            if last_profit > maximum_profit:
                maximum_profit = last_profit
        return maximum_profit if maximum_profit > 0 else 0    

# time complexity = O(n)
# space complexity = O(n)






#using prefix (like kadane's algorithm)
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = float("inf")
        best_profit = 0
        for p in prices:
            min_price = min(p, min_price)
            best_profit = max(best_profit, p - min_price)
        return best_profit

# time complexity = O(n)
# space complexity = O(1)





# Brute Force
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        len_prices = len(prices)
        maximum_price = float("-inf")
        for i in range(len_prices):
            for j in range(i + 1, len_prices):
                last_prices = prices[j] - prices[i]
                if last_prices > maximum_price:
                    maximum_price = last_prices
        return maximum_price if maximum_price > 0 else 0
    
# time complexity = O(n^2)
# space complexity = O(1)