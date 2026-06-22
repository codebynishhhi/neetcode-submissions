# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        slow = dummy
        fast = dummy

        for _ in range(n+1):
            fast = fast.next
        
        while fast:
            # till fast reaches None , move both slow & fast
            slow = slow.next
            fast = fast.next
        
        # once u reach the element before the target , update the pointer
        slow.next = slow.next.next
        return dummy.next


        