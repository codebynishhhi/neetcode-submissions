class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # step 1 - create frequency hmap using "Counter"
        count = Counter(tasks)
        # {"A":3, "B":1, "C":1} - o/p after counter

        # step 2 - negate to create max_heap
        max_heap = [-freq for freq in count.values()]

        # step 3 - create max heap using heapify
        heapq.heapify(max_heap)

        # queue to store cooldown 
        queue = deque()

        time = 0
        while max_heap or queue:
            time += 1
            # step 4 - if max_heap has value pop the top
            if max_heap:
                freq = heapq.heappop(max_heap)
                freq += 1
                if freq != 0:
                    queue.append((freq, time+n))
                
            if queue and queue[0][1] == time:
                heapq.heappush(max_heap, queue.popleft()[0])
        return time



        