class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # number of row  
        m = len(matrix)
        # number of cols
        n = len(matrix[0])
        # start of 2d array left pointer 
        left = 0
        # end of 2d array right pointer
        right = (m*n) -1 
        while left <= right:
            mid_index = left + (right - left) // 2
            row, col = divmod(mid_index , n)
            ans = matrix[row][col]
            if target == ans:
                return True
            elif target < ans :
                right = mid_index - 1
            else:
                left = mid_index + 1
        return False