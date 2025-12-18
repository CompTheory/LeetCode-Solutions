# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slower = faster = head
        while faster and faster.next:
            slower = slower.next
            faster = faster.next.next
            if slower == faster:
                break
        else:
            return None
        
        faster = head
        
        while faster != slower:
            faster = faster.next
            slower = slower.next
        
        return slower
