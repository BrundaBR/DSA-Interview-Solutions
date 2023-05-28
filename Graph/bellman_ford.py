def bellman_ford(self, src):
    distance = [float("Inf")] * self.M
    distance[src] = 0
    for _ in range(self.M - 1):
 
        for a, b, c in self.graph:
 
            if distance[a] != float("Inf") and distance[a] + c < distance[b]:
 
                distance[b] = distance[a] + c
 
 
 
    for a, b, c in self.graph:
 
        if distance[a] != float("Inf") and distance[a] + c < distance[b]:
 
            print("Graph contains negative weight cycle")
 
            return
    self.print_solution(distance)

'''
import collections
class Solution:
    def bellman_ford(self, V, adj, S):
        # initialize all distance = infi
        dist = [100000000]*V
        # initialize the start to start = 0 
        dist[S] = 0
        for i in range(V-1):
            for src, dest, distance in adj:
                dist[dest] = min(dist[dest], dist[src]+distance)
        return dist
'''
