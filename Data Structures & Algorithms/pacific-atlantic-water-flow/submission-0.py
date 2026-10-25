class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows, cols = len(heights), len(heights[0])
        pacific = set()
        atlantic = set()

        # directions for all neighbouring cells to traverse 
        directions = [(1,0), (-1,0), (0, 1), (0,-1)]

        def dfs(row:int, col:int, reachable:set):
            reachable.add((row, col))

            for dr, dc in directions:
                nr , nc = row+dr, col+dc

                # boundary checking 
                # 1. nr - new row, should be in the range of 0 to rows
                # 2. nc - new col, should be in the range of 0 to cols
                # 3. (nr, nc) should not be in the reachable set, only then we continue 
                # 4. heights[nr][nc] >= height[row][col] - water can flow from high to low
                if (0 <= nr < rows and 0 <= nc < cols
                and (nr, nc) not in reachable and 
                heights[nr][nc] >= heights[row][col]):
                    dfs(nr, nc, reachable)

                
        # for pacific borders(top + left borders)

        # for cols - left path (r)
        for c in range(cols):
            dfs(0, c, pacific)
        # for rows - top path
        for r in range(rows):
            dfs(r, 0, pacific)

        # for atlantic borders(right + bottom borders)

        # for c - right path (r-1)
        for c in range(cols):
            dfs(rows-1, c, atlantic)
        for r in range(rows):
            dfs(r, cols-1, atlantic)

        # Cells reachable by both oceans using the intersection operator (&)
        return [(row, col) for row, col in (pacific & atlantic)]
        

