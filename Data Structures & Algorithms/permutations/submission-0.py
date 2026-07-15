class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        subset = []

        def dfs_backtrack():
            # base condition
            # if index == list len, travesed all 
            if len(subset) == len(nums):
                result.append(subset.copy())
                return

            for num in nums:
                if num not in subset:
                    # add in subset
                    subset.append(num)

                    dfs_backtrack()
                    # if num exists in subset - pop it 
                    subset.pop()
        dfs_backtrack()
        return result

        