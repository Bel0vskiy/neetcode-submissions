class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        m = {i: [] for i in range(numCourses)}
        for c, p in prerequisites:
            m[c].append(p)
        
        seen = set()

        def dfs(c):
            if c in seen:
                return False
            if m[c] == []:
                return True
            seen.add(c)
            for p in m[c]:
                if not dfs(p):
                    return False
            seen.remove(c)
            m[c] = []
            return True
        for c in range(numCourses):
            if not dfs(c):
                return False
        return True