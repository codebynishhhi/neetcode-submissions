class Solution:
    def combinationSum2(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        result = []
        subset = []

        def dfs(index, target):
            # base condition 1
            if target == 0:
                result.append(subset.copy())
                return
            
            # base case 2 - when invalid target
            if target < 0:
                return

            # base case 3 - index reached list
            if index == len(nums):
                return 
            
            # Choice 1 - take the decission 
            subset.append(nums[index])
            dfs(index + 1, target - nums[index])

            subset.pop()

            # skip dupliactes
            while (index +1 < len(nums) and nums[index]== nums[index +1]):
                index += 1

            # Choice 2 - skip decissio
            dfs(index + 1, target)
        dfs(0, target)
        return result

             