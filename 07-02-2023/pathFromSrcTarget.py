class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        n=len(graph)
        q=deque()
        q.append([0,[0]])
        l=[]
        while q:
            m,p=q.popleft()
            if m==n-1:
                l.append(p)
            for i in graph[m]:
                q.append([i, p+[i]])
        return l
