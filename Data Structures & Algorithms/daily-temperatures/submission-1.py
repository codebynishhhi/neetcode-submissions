class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # Brute force - 
        # T.C = O(n^2), S.C = O(N)
        newlist = [0] * len(temperatures)
        stack = []
        # for i in range(len(temperatures)):
        #     for j in range(i+1,len(temperatures)):
        #         if temperatures[j] > temperatures[i]:
        #             # distance between j - 1 is actuall number of days
        #             # between the current to next warmer day
        #             newlist[i] = j-i
        #             break
        # return newlist 

        # Optimized solution using MONOTONIC STACK
        # T.C = O(N), S.C = O(N)
        # enumerate bcz we are iterating & storing key value pair
        # distance between j - 1 is actuall number of days here
        # here j = prev_index
        for i, temp in enumerate(temperatures):
            while stack and temp > stack[-1][1]:

                prev_index, prev_temp = stack.pop()

                newlist[prev_index] = i - prev_index 
                
            stack.append((i, temp))
        return newlist
                
            

        