"""
LeetCode #1 – Two Sum
"""



# optimize Solution
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        new_hashmap = dict()

        for i, key in enumerate(nums):
            diff = target - key
            if diff in new_hashmap:
                return [new_hashmap[diff], i]
            new_hashmap[key] = i


# time complexity = O(n)
# space compleixty = O(n)






# Brute Force Solution
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        for i in range(n):
            for j in range(i + 1, n):
                if nums[i] + nums[j] == target:
                    return [i, j]


# time complexity = O(n ^ 2)
# space Complexity = O(1)


# Example usage:
# nums = [2, 7, 11, 15], target = 9
# Output: [0, 1]
