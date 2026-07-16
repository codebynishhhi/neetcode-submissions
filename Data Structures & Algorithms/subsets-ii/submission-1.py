class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        # not contain duplicates -
        #  1. always sort - to arrange duplicates side by side 
        #  2. write logic to skip duplicates 
        nums.sort()
        result = []
        subset = []

        def dfs(index):
            # base case - 1
            if index == len(nums):
                result.append(subset.copy())
                return
            
            # Choice 1 - subset add- take 
            subset.append(nums[index])
            dfs(index + 1)

            # subset pop
            subset.pop()

            # skip duplicates
            while (index + 1) < len(nums) and nums[index] == nums[index+1]:
                index += 1

            # Choice 2 - leave it 
            dfs(index +1)
        dfs(0)
        return result

 
        