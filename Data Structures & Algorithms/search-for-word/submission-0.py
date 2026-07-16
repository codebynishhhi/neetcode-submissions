class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows = len(board)
        cols = len(board[0])

        def dfs_char(r, c, index):
            # Base conditions 
            # word matched - only when index = len of word
            if index == len(word):
                return True

            # invalid cases
            # 1. if r<0 or c<0, or r>=rows, c>=cols
            # 2. if board[r][c] char != word[index] char
            if (r < 0 or c < 0 or r >= rows or c >= cols or 
                board[r][c] != word[index]):
                return False

            # Mark visited by #, extract 
            temp = board[r][c]
            board[r][c] = "#"

            # explore all four dircetions from that char
            found = (
                # immediate next row
                dfs_char(r+1, c, index + 1) or 
                # immediate up row
                dfs_char(r-1, c, index + 1) or
                # immediate left 
                dfs_char(r, c-1, index + 1) or
                # immediate right
                dfs_char(r, c+1, index + 1)
            )

            # backtrack by removing # to temp value again in the board
            board[r][c] = temp
            return found


        for r in range(rows):
            for c in range(cols):
                if dfs_char(r, c, 0):
                    return True
        return False



