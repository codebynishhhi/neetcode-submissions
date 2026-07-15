class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        # This problem is combination of 
        # Subset + Combination Sum
        candidates.sort()
        result = []
        subset = []

        def dfs(index, target):
            # base case 3 -> we got 0 diff
            if target == 0:
                result.append(subset.copy())
                return

            # base case 1 -> index reached end of list
            if index == len(candidates):
                return
            
            # base case 2 -> if 
            if target < 0:
                return
            
            # Choice 1 - take/add to subset
            subset.append(candidates[index])
            dfs(index+1, target - candidates[index])

            # undo
            subset.pop()

            # leave/skip the duplicates
            # index + 1 = next ele is there or not
            while (index + 1 < len(candidates) and candidates[index] == candidates[index+1]):
                index += 1
            
            # Choice 2 - skip/leave the decission
            dfs(index +1 , target )
        dfs(0, target)
        return result


             