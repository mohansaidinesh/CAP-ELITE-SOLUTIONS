class Solution:
    
    #Function to return a list containing the DFS traversal of the graph.
    def dfsOfGraph(self, V, adj):
        # code here
        l=[]
        def trav(n):
            if n not in l:
                l.append(n)
                for i in adj[n]:
                    trav(i)
        trav(0)
        return l
