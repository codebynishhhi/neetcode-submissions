class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        def dfs(path, openCount, closeCount):

            # base case - len of path should be equal to 2*n
            if len(path) == 2*n:
                result.append(path)
                return
            
            if openCount < n:
                dfs(path+"(", openCount+1, closeCount)
            if closeCount < openCount:
                dfs(path+")", openCount, closeCount+1)
        dfs("", 0,0)
        return result
            

        