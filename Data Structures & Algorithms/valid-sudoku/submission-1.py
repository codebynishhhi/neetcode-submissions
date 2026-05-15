class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # creating hashset for each row,
        # for each column & 
        # for each squares so that there is no duplicates
        rows = defaultdict(set)
        cols = defaultdict(set)
        boxes = defaultdict(set)

        # traversing the array with 9*9 & picking each element
        for r in range(9):
            for c in range(9):
                value = board[r][c]
                if value == ".":
                    continue

                box = (r//3, c//3)
                # check duplicates in set
                # if duplicates exists in either rows, cols, boxes indexes
                if (value in rows[r] or value in cols[c] or value in boxes[box]):
                    return False
                rows[r].add(value)
                cols[c].add(value)
                boxes[box].add(value)
        return True
                


        