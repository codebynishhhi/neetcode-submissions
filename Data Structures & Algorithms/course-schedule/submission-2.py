class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = [[] for _ in range(numCourses)]

        for a, b in prerequisites:
            graph[b].append(a)

        visiting = set()
        processed = set()

        def dfs(course):
            if course in processed:
                return True
            if course in visiting:
                return False
            
            visiting.add(course)

            # add course to visiting
            # then explore all the neighbours 
            for neighbour in graph[course]:
                if not dfs(neighbour):
                    return False
            
            visiting.remove(course)
            processed.add(course)
                
            return True

        
        # Step 3: Check every disconnected component
        for course in range(numCourses):
            if course not in processed:
                if not dfs(course):
                    return False

        return True

            
            
