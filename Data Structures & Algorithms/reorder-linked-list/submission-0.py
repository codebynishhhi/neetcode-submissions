# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# Mental Model:
# 1. Find middle using slow & fast pointers
# 2. Reverse second half
# 3. Merge alternating nodes
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head:
            return

        # 1. find the middle using slow & fast pointers
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # 2. reverse the second half generated from split
        second = slow.next
        slow.next = None
        prev = None
        curr = second
        while curr :
            # always first save next node address
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        second = prev
        first = head
        while second:
            tmp1 = first.next
            tmp2 = second.next

            first.next = second
            second.next = tmp1

            first = tmp1
            second = tmp2



        