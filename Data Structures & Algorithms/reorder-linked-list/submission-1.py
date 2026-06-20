# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# Mental Model:
# 1. Find middle using slow & fast pointers - 2 pointers
# 2. Reverse second half
# 3. Merge alternating nodes
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head:
            return
        
        # 1. find middle to split the LL into 2 halves using 2 pointers
        # 2 halves will be there 
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # 2. reverse the second half
        second = slow.next
        slow.next = None
        prev = None
        # curr is the first pointer of second list
        curr = second
        while curr :
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        # 3. merge the 2 halves of array
        second = prev
        first = head
        while second:
            tmp1 = first.next
            tmp2 = second.next

            first.next = second
            second.next = tmp1

            first = tmp1
            second = tmp2



        