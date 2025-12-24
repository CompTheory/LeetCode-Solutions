"""
LeetCode #217 - Contains Duplicate
"""




# time optimal
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hashset = set()
        for i in nums:
            if i in hashset:
                return True
            hashset.add(i)
        return False


# time complexity = O(n)
# space complexity = O(n)




# space optimal
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        n = len(nums)
        for i in range(1, n):
            if nums[i] == nums[i - 1]:
                return True
        return False


# time complexity = O(n) in best case and O(nlogn) in worst case

# space complexity = O(1)
