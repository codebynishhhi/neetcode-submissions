from collections import deque
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        # create a dictonary of opening closing mapping 
        open_close_map = {
            ']':'[',
            '}':'{',
            ')':'('
        }
        for char in s:
            if char in open_close_map:
                # If new iteration char is from the dictonary then

                # check 1 - is stack empty
                # if stack is empty - return FALSE
                if not stack:
                    return False
                # CHECK 2 - if new char and stack's top char is not same 
                # then also return false
                if stack[-1] != open_close_map[char]:
                    return False
                
                # if check 1 & 2 fail- means match found --> pop that element
                stack.pop()
                
            else:
                stack.append(char)
        return len(stack) == 0 




        