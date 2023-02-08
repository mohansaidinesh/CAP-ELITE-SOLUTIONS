class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        parent=[i for i in range(len(edges)) ]
        def find(node):
            while parent[node]!=node:
                node=parent[node]
            return node
        for v1,v2 in edges:
            v1-=1
            v2-=1
            pa1=find(v1)
            pa2=find(v2)
            if pa1==pa2:
                return [v1+1,v2+1]
            else:
                parent[pa1]=pa2
