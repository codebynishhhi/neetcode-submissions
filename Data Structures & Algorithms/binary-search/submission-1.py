class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) -1
        while left <= right:
            mid_index = (left+right) // 2
            if target == nums[mid_index]:
                return mid_index
            elif target < nums[mid_index]:
                right = mid_index - 1
            else :
                left = mid_index +1
        return -1
            
        