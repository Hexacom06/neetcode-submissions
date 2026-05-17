class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        indeg = [0] * numCourses
        adj = [[] for _ in range(numCourses)]
        res = []
        for course, prereq in prerequisites:
            adj[prereq].append(course)
            indeg[course] += 1
        q = deque()
        for i in range(numCourses):
            if indeg[i] == 0:
                q.append(i)
        while q:
            curr = q.popleft()
            res.append(curr)
            for nei in adj[curr]:
              indeg[nei] -= 1
              if indeg[nei] == 0:
                q.append(nei)
        return res if len(res) == numCourses else []