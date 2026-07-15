class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        results = []
        subset = []

        def dfs(index):
            # base case 
            if index == len(nums):
                results.append(subset.copy())
                return
            
            # take the decission -> so append in subset list
            subset.append(nums[index])

            dfs(index + 1)

            # undo
            subset.pop()

            dfs(index + 1)

        dfs(0)
        return results


        