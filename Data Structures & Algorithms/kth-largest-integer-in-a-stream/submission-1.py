class KthLargest:

    def __init__(self, k: int, nums: List[int]):

        # initialize k and heap 
        self.k = k
        self.heap = nums

        # heapify the nums list to convert to heap list format
        heapq.heapify(self.heap)

        while len(self.heap) > k:
            heapq.heappop(self.heap)

    def add(self, val: int) -> int:
        # heappushpop pushes val, then pops and returns the smallest item.
        # It is faster than doing push and pop separately!
        if len(self.heap) < self.k:
            heapq.heappush(self.heap, val)
        else:
            heapq.heappushpop(self.heap, val)
            
        return self.heap[0]

        
