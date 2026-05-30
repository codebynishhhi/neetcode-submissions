class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # since array is sorted and o(1) time constraint 
        # we use 2 pointer 
        left = 0
        right = len(numbers) - 1
        while left < right:
            sum = numbers[left] + numbers[right]
            if sum == target:
                return [left+1, right+1]
            elif sum > target:
                right -= 1
            else:
                left += 1
