# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# This problem can be solved using - FAST & SLOW pointers
# where both initially point to head of LL
# slow - slow.next and fast = fast.next.next
# if both are equal --> then cycle else False
#  T.C - O(N) , S.C - O(1)
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast :
                return True
        return False
        