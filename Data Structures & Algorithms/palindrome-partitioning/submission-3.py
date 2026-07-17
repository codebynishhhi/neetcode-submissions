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
        
        def dfs(start_index):
            # base case 
            if start_index == len(s):
                result.append(path.copy())
                return
            
            # we append the slicing all possible strings
            for end in range(start_index , len(s)):
                if isPalindrome(start_index, end):
                    path.append(s[start_index: end +1])
                    dfs(end + 1)
                    path.pop()
        dfs(0)
        return result


            


