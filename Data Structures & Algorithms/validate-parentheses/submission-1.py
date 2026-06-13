from collections import deque
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        close_to_open_map = {
            ']':'[',
            '}':'{',
            ')':"("
        }
        for char in s:
            if char in close_to_open_map:
                # check 1 - empty stack
                if not stack:
                    return False
                
                # check 2 - last element match
                if stack[-1] !=  close_to_open_map[char]:
                    return False
                
                # both check 1 & 2 fail then match found
                stack.pop()

            else:
                stack.append(char)

        return len(stack) == 0



        