class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow = nums[0]
        fast = nums[0]

        # phase 1 - find the index where both slow & fast are equal
        while True:
            # slow moves by 1
            # fast moved by 2 
            slow = nums[slow]
            fast = nums[nums[fast]]

            # find the point where both pointers collide
            if slow == fast:
                break

        # Phase 2 - find the 
        slow2 = nums[0]
        while slow != slow2:
            slow = nums[slow]
            slow2 = nums[slow2]
        return slow