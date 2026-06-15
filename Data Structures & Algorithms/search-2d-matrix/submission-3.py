class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # number of rows
        m = len(matrix)
        # number of columns
        n = len(matrix[0])
        left = 0
        right = (m*n) - 1
        while left <= right:
            mid_index = left +(right - left) //2
            row = mid_index // n
            col = mid_index % n

            ans = matrix[row][col]

            if target == ans:
                return True 
            elif target < ans:
                right = mid_index - 1
            else :
                left = mid_index+1
        return False

        