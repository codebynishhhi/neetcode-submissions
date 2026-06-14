class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # making a pos, speed list 
        # cars = [(1, 3)---> (pos, speed)]
        cars = list(zip(position, speed))
        cars.sort(reverse = True)
        stack = []
        for pos, spd in cars :
            time = (target - pos) / spd

            if not stack:
                stack.append(time)
            if time > stack[-1]:
                stack.append(time)
        return len(stack)



        