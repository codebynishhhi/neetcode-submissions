class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:

        # using BFS For this problem reason in
        queue = deque()
        rows = len(grid)
        cols = len(grid[0])

        # add all treasure which is 0 to the queue to sort of initialization 
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 0:
                    queue.append((row, col))

        # no recurssion so we select adjacent neighbours by this dict
        directions = [(1,0), (-1,0), (0,1), (0,-1)]

        # start bfs queue iteration
        # queue = [(0,2)]
        while queue:

            # fetch the current (row, col) value from queue
            row, col = queue.popleft()

            # explore the adjacent cell up, down top , bottom 
            for dr, dc in directions:
                new_row = row + dr
                new_col = col + dc

                # Base cases - 2 are there 

                # BASE CASE 1  - index out of bounds check for new row and col
                if (
                    new_row <0 or new_row >= rows or
                    new_col <0 or new_col >= cols 
                    ):
                    continue
                 
                # BASE CASE - 2
                # if grid(row, col) value is not inf number means it already has smallest distance int value
                if grid[new_row][new_col] != 2147483647:
                    continue
                
                # both base case fail so add new distance to cell
                grid[new_row][new_col] = grid[row][col] + 1
                
                queue.append((new_row, new_col))




        