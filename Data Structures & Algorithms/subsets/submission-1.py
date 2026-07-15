class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        subset = []

        def dfs(index):
            # base condition
            if index == len(nums):
                result.append(subset.copy())
                return
            
            # choice 1- add all ele/decissions to subset first
            subset.append(nums[index])
            dfs(index +1)

            # after adding alll undo - to backtrack 
            subset.pop()

            # Choice 2 - skip, by moving
            dfs(index + 1)
        dfs(0)
        return result

        