class Graph():
	def minDistance(self, dist, sptSet):
		min = 1e7
		for v in range(self.V):
			if dist[v] < min and sptSet[v] == False:
				min = dist[v]
				min_index = v
		return min_index
	def dijkstra(self, src):
		dist = [1e7] * self.V
		dist[src] = 0
		sptSet = [False] * self.V
		for cout in range(self.V):
			u = self.minDistance(dist, sptSet)
			sptSet[u] = True
			for v in range(self.V):
				if (self.graph[u][v] > 0 and
				sptSet[v] == False and
				dist[v] > dist[u] + self.graph[u][v]):
					dist[v] = dist[u] + self.graph[u][v]
		self.printSolution(dist)
