"""
LeetCode #152 - Maximum Product Subarray
"""



# approach like kadane's algorithm
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        maximum_product = maximum_revproduct = float("-inf")
        last_product = 1
        for n in nums:
            last_product *= n
            maximum_product = max(maximum_product, last_product)
            if last_product == 0:
                last_product = 1
        last_product = 1
        nums = nums[::-1]
        for n in nums:
            last_product *= n
            maximum_revproduct = max(maximum_revproduct, last_product)
            if last_product == 0:
                last_product = 1
        return max(maximum_product, maximum_revproduct)
        
# time complexity = O(n)
# space complexity = O(1)




# greedy approach tracking max and min 
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        cur_max = cur_min = max_prod = nums[0]
        for n in nums[1:]:
            temp = max(n, cur_min * n , cur_max * n)
            cur_min = min(n, cur_min * n, cur_max * n)
            cur_max = temp
            max_prod = max(cur_max, max_prod)
        return max_prod        

# time complexity = O(n)
# space complexity = O(1)




#Brute Force
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        maximum_product = float("-inf")
        last_product = 1
        len_nums = len(nums)
        for i in range(len_nums):
            last_product = 1
            for j in range(i, len_nums, 1):
                last_product *= nums[j]
                if last_product > maximum_product:
                    maximum_product = last_product
        return maximum_product

# time complexity = O(n)
# space complexity = O(1)