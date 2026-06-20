# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


# using Dummy Node Problem 
# 1 dummy node and 1 pointer tail
# 1. create a fake node to attach all the ans
# 2. tail initially poits to dummy , then keeps increasing always pointing to last node
# 3. attach smaller value to dummy
# 4. move tail pointer
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        tail = dummy
        while list1 and list2:
            if list1.val <= list2.val:
                # pick list 1 val and add to dummy by moving tail pointer
                tail.next = list1
                list1 = list1.next
            else:
                # pick from list2 
                tail.next = list2
                list2 = list2.next
            # now move tail of next
            tail = tail.next

        # if elements still in list 1 , add to dummy
        if list1:
            tail.next = list1
        else:
            tail.next = list2
        return dummy.next



        