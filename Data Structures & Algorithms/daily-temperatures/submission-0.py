class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        newlist = [0] * len(temperatures)
        for i in range(len(temperatures)):
            for j in range(i+1,len(temperatures)):
                if temperatures[j] > temperatures[i]:
                    # distance between j - 1 is actuall number of days
                    # between the current to next warmer day
                    newlist[i] = j-i
                    break
        return newlist 
        