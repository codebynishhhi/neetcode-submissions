
from typing import List

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        rows, cols = len(board), len(board[0])

        def dfs(row, col):
            # Stop if outside the board or not an O
            if (
                row < 0 or row >= rows or
                col < 0 or col >= cols or
                board[row][col] != "O"
            ):
                return

            # Mark this O as safe
            board[row][col] = "S"

            # Explore all four neighbours
            dfs(row + 1, col)
            dfs(row - 1, col)
            dfs(row, col + 1)
            dfs(row, col - 1)

        # Step 1: Explore O's on the top and bottom borders
        for col in range(cols):
            if board[0][col] == "O":
                dfs(0, col)

            if board[rows - 1][col] == "O":
                dfs(rows - 1, col)

        # Step 2: Explore O's on the left and right borders
        for row in range(rows):
            if board[row][0] == "O":
                dfs(row, 0)

            if board[row][cols - 1] == "O":
                dfs(row, cols - 1)

        # Step 3: Capture surrounded O's and restore safe O's
        for row in range(rows):
            for col in range(cols):
                if board[row][col] == "O":
                    board[row][col] = "X"
                elif board[row][col] == "S":
                    board[row][col] = "O"

from typing import List

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        rows, cols = len(board), len(board[0])

        def dfs(row, col):
            # Stop if outside the board or not an O
            if (
                row < 0 or row >= rows or
                col < 0 or col >= cols or
                board[row][col] != "O"
            ):
                return

            # Mark this O as safe
            board[row][col] = "S"

            # Explore all four neighbours
            dfs(row + 1, col)
            dfs(row - 1, col)
            dfs(row, col + 1)
            dfs(row, col - 1)

        # Step 1: Explore O's on the top and bottom borders
        for col in range(cols):
            if board[0][col] == "O":
                dfs(0, col)

            if board[rows - 1][col] == "O":
                dfs(rows - 1, col)

        # Step 2: Explore O's on the left and right borders
        for row in range(rows):
            if board[row][0] == "O":
                dfs(row, 0)

            if board[row][cols - 1] == "O":
                dfs(row, cols - 1)

        # Step 3: Capture surrounded O's and restore safe O's
        for row in range(rows):
            for col in range(cols):
                if board[row][col] == "O":
                    board[row][col] = "X"
                elif board[row][col] == "S":
                    board[row][col] = "O"
