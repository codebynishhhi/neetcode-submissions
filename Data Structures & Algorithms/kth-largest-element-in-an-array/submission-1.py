class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap_large = []
        nums = [-ele for ele in nums]
        # nums = [-2, -3, -1, -5, -4]
        heapq.heapify(nums)
        # nums = [-5, -4, -1, -3, -2]
        for _ in range(k-1):
            heapq.heappop(nums)
        #  return top heap val 
        return -nums[0]

        