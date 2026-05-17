class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        indeg = [0] * numCourses
        adj = [[] for _ in range(numCourses)]
        for course, prereq in prerequisites:
            adj[prereq].append(course)
            indeg[course] += 1
        completed = 0
        q = deque()
        for i in range(numCourses):
            if indeg[i] == 0:
                q.append(i)
        while q:
            curr = q.popleft()
            completed += 1
            for nei in adj[curr]:
              indeg[nei] -= 1
              if indeg[nei] == 0: 
                q.append(nei)
        return completed == numCourses 
