class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:

        # creating adjacency list graph -
        graph = [[] for _ in range(numCourses)]

        # unpacking prerequisites, to fill in the adjacency list
        # since b completes before a , b-> a so graph[b].append(a)
        for a, b in prerequisites:
            graph[b].append(a)

        visiting = set()
        processed = set()
        order = []

        # dfs over each course
        def dfs(course):
            if course in processed:
                return True

            if course in visiting:
                return False
            
            # once course addeed to visting path
            visiting.add(course)

            # explore the visting course neighbours and run dfs on them
            for neighbour in graph[course]:
                if not dfs(neighbour):
                    return False
            
            # once all neighbours of a course is explored
            # remove course from visiting
            visiting.remove(course)

            # add course to processed now
            processed.add(course)

            # append the course to get the order in end
            order.append(course)

            return True

            # now explore all the courses in the graph
            # run dfs on every course stored in num courses
            # if course is not already proceseed -> give it to dfs
            # if dfs returns false then return [] -> cycle found
        for course in range(numCourses):
            if course not in processed:
                if not dfs(course):
                    return [] 
                
            
        order.reverse()
        return order
        

            



        