class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []
        subset = []

        def dfs(index, target):

            # Found a valid combination
            if target == 0:
                result.append(subset.copy())
                return

            # Invalid path
            if target < 0:
                return

            # No more numbers
            if index == len(nums):
                return

            # --------------------
            # Choice 1 : Take
            # --------------------
            subset.append(nums[index])

            dfs(index, target - nums[index])

            # Backtrack
            subset.pop()

            # --------------------
            # Choice 2 : Skip
            # --------------------
            dfs(index + 1, target)

        dfs(0, target)
        return result
