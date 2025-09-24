# 4. CourseSchedule.py
from collections import defaultdict, deque

class Solution:
    def canFinish(self, numCourses, prerequisites):
        graph = defaultdict(list)
        indegree = [0]*numCourses
        for u, v in prerequisites:
            graph[v].append(u)
            indegree[u] += 1
        
        q = deque([i for i in range(numCourses) if indegree[i]==0])
        visited = 0
        while q:
            node = q.popleft()
            visited += 1
            for nei in graph[node]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    q.append(nei)
        return visited == numCourses
