class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        # len of row and col 
        rows = len(grid)
        cols = len(grid[0])
        visited = set()
        count_island = 0

        # dfs function will only add the position to set if not visisted
        # or explore all the paths from a given coordinate
        def dfs(row, col):

            # base conditions
            if (row < 0 or
                row >= rows or 
                col < 0 or 
                col >= cols or
                (row,col) in visited or 
                grid[row][col] == "0"
                ):
                return 
            
            # if all base conditions fail - add index row, col to set to mark visited
            visited.add((row, col))

            # after marking visited - explore all 4 neighbiurs
            dfs(row+1, col)
            dfs(row-1, col)
            dfs(row, col+1)
            dfs(row, col-1)

        # getting coordinates row and col index
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == "1" and (row, col) not in visited:
                    dfs(row, col)
                    count_island += 1
        return count_island 

        



