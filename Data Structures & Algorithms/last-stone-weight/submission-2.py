class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
       # solve this using max heap 

        # convert stones list to max heap by negate 
        # multiplying -1 to all list elements to get max heap
        stones = [-stone for stone in stones]

        # after negate, heapify the list
        heapq.heapify(stones)
        while len(stones) > 1:
            # pop first & sencond largest from max heap
            first = -heapq.heappop(stones)
            second = -heapq.heappop(stones)

            if first != second:
                # if unequal push their differnce to heap
                # to create new updated heap list
                heapq.heappush(stones, -(first - second))
        if stones:
            return -stones[0]
        return 0

        