class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1
        # unlinke normal binary search where left <= right
        # here left < right , bcz min could be mid itself
        # so mid = right , keep shirinking
        while left < right:
            mid = (left + right) // 2
            # if mid is big then small values are in right 
            # move left to mid+1 , to get close mid to small values
            if nums[mid] > nums[right]:
                left = mid +1
            else :
                right = mid
        return nums[left]

        