class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # for count of fresh fruits 
        fresh = 0
        minutes = 0

        rows = len(grid)
        cols = len(grid[0])

        que = deque()

        # add all rotten fruits to queue and count all fresh fruits 
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 2:
                    que.append((row, col))
                elif grid[row][col] == 1:
                    fresh += 1

        # no fresh fruits then return 0 no computattion
        if fresh == 0:
            return 0
        
        # one bfs level - one min, bfs traversal for 1 rotten fuit from queu
        while que and fresh > 0:

            for _ in range(len(que)):
                row, col = que.popleft()

                # down(bottom adjacent cell)
                if row + 1 < rows and grid[row+1][col] == 1:
                    grid[row+1][col] = 2
                    fresh -= 1
                    que.append((row+1, col))
                
                #  up (top adjacent cell)
                if row - 1 >=0 and grid[row-1][col] == 1:
                    grid[row-1][col] = 2
                    fresh -= 1
                    que.append((row-1, col))
                
                #  left 
                if col + 1 < cols and grid[row][col+1] == 1:
                    grid[row][col+1] = 2
                    fresh -= 1
                    que.append((row, col+1))
                
                # right
                if col -1 >=0 and grid[row][col -1]== 1:
                    grid[row][col - 1] = 2
                    fresh -= 1
                    que.append((row,col-1))

            # once for loop completes bfs level 1 is done inc min
            minutes += 1

        return minutes if fresh == 0 else -1   
                





