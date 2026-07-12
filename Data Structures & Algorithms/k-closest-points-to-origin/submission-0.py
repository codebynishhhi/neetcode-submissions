class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        # we will push distance, points into this heap
        heap_dis = []
        for x, y in points:
            distance = x*x + y*y

            # push to heap
            heapq.heappush(heap_dis,(-distance, [x, y]) )

            if len(heap_dis) > k:
                heapq.heappop(heap_dis)
        result = []
        while heap_dis:
            result.append(heapq.heappop(heap_dis)[1])
        return result