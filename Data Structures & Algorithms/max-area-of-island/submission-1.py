class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0

        rows = len(grid)
        cols = len(grid[0])
        max_area = 0
        visited = set()

        
        # dfs function will only - 
        # 1. add the coordinate to set if not visisted & explore all the paths from a given coordinate
        # 2. or check the base conditions and return 
        def dfs(row, col):

            # check all base conditions
            # 1. if curr row's index is out of bounds - less than 0 or >= len of row in grid
            # 2. if (row, col) coordinate is in set - coordinate already visited
            # 3. if grid[row][col] value at the coordinate is 0 then water 
            # return in all these cases
            if (row < 0 or
                row >= rows or
                col < 0 or 
                col >= cols or 
                (row, col) in visited or
                grid[row][col] == 0
            ):
                return 0

            # if all bases case fails - add coordinate to set as tuple
            visited.add((row, col))

            # after adding new coordinate to set - 1 (curr cordinate + explore all 4 directions)
            curr_area = (1 + dfs(row+1, col) + dfs(row-1, col) + dfs(row, col+1)+ dfs(row, col-1))

            return curr_area

        for row in range(rows):
            for col in range(cols):
                # if value in grid is 1 = island and its coordinate not in set
                # means new island found then call dfs and inc count
                if (row, col) not in visited and grid[row][col] == 1:
                    island_area = dfs(row, col)
                    max_area = max(max_area, island_area)

        return max_area
        