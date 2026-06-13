class MinStack:

    def __init__(self):
        self.main_stack = []
        self.min_stack = []        

    def push(self, val: int) -> None:
        # add new val to main stack
        self.main_stack.append(val)
        
        # check if min stack is empty then add
        if not self.min_stack :
            self.min_stack.append(val)
        else:
            # if min stack has value find the min among the current val
            #  and the existing val in min stack
            current_min = self.min_stack[-1]
            self.min_stack.append(min(current_min, val))
        

    def pop(self) -> None:
        # pop from both min and main stack to keep aligned
        self.main_stack.pop()
        self.min_stack.pop()
        

    def top(self) -> int:
        # returns the last elemnt of the main stack
        return self.main_stack[-1]

    def getMin(self) -> int:
        # returns always min stack topmost element
        return self.min_stack[-1]
        
        
