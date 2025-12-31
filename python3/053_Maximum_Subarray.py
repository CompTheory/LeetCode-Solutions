# Kadane’s Algorithm
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = float("-inf")
        last_sum = 0
        for i in nums:
            if last_sum < 0:
                last_sum = 0
            last_sum += i
            if last_sum > max_sum:
                max_sum = last_sum
        return max_sum
    
# time complexity = O(n)
# space complexity = O(1)


# divide and conquer
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1
        def sub(arr, l, r):
            def cross_max(arr, l , q, r):
                sum_left = sum_right = float("-inf")
                last_sum = 0
                for i in range(q, l - 1, -1):
                    last_sum += nums[i]
                    if last_sum > sum_left:
                        sum_left = last_sum
                last_sum = 0
                for i in range(q + 1, r + 1, 1):
                    last_sum += nums[i]
                    if last_sum > sum_right:
                        sum_right = last_sum
                if sum_left < 0:
                    return sum_right
                elif sum_right < 0:
                    return sum_left
                return (sum_left + sum_right)
            if l == r:
                return nums[0]
            q = (l + r) // 2
            sum_l = sub(nums, l, q)
            sum_r = sub(nums, q + 1, r)
            cross_sum = cross_max(arr, l, q, r)
            if sum_l >= cross_sum and sum_l >= sum_r:
                return sum_l
            elif sum_r >= cross_sum and sum_r >= cross_sum:
                return sum_r
            return cross_sum
        return sub(nums, l, r)
    
# time complexity = O(nlogn)
# space complexity = O(logn) for recursive



# brute force
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        len_nums = len(nums)
        max_sum = float("-inf")
        for i in range(len_nums):
            last_sum = 0
            for j in range(i, len_nums, 1):
                last_sum += nums[j]
                if last_sum > max_sum:
                    max_sum = last_sum
        return max_sum

# time complexity = O(n^2)
# space complexity = O(1)
