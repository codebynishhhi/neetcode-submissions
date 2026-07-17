class Solution:
    def partition(self, s: str) -> List[List[str]]:
        result = []
        path = []

        def isPalindrome(left, right):
            while left < right:
                if s[left] != s[right]:
                    return False
                
                left += 1
                right -= 1
            return True
        
        def dfs(index):
            # base case if index == len of string, means traversal complete
            if index == len(s):
                result.append(path.copy())
                return
            
            # try every possible string - slicing logic
            # start from index = 0, and slicing at each new index and len
            for end in range(index, len(s)):
                if isPalindrome(index, end):
                    path.append(s[index:end+1])
                    dfs(end + 1)
                    path.pop()

        dfs(0)
        return result



            


