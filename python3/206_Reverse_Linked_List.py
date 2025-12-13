"""
LeetCode #206 - Reverse Linked List
Youtube Video: https://www.youtube.com/watch?v=1SdQ23HUl04
"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur = head
        prev = None
        while cur:
            new_node = cur.next
            cur.next = prev
            prev = cur
            cur = new_node
        return prev
    

# time complexity = O(n)
# space complexity = O(1)

        
# Example Usage:
# Input: head = [1,2,3,4,5]
# Output: [5,4,3,2,1]

