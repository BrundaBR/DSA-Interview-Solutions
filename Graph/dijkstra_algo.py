from queue import PriorityQueue
class Graph:
    def __init__(self, num_of_vertices):
        self.v = num_of_vertices
        self.edges = [[-1 for i in range(num_of_vertices)] for j in range(num_of_vertices)]
        self.visited = []
    def add_edge(self, u, v, weight):
        self.edges[u][v] = weight
        self.edges[v][u] = weight
 
def dijkstra(graph, start_vertex):
    D = {v:float('inf') for v in range(graph.v)}
    D[start_vertex] = 0
 
    pq = PriorityQueue()
    pq.put((0, start_vertex))
 
    while not pq.empty():
        (dist, current_vertex) = pq.get()# get from priority queu
        graph.visited.append(current_vertex) #mark as visited
 
        for neighbor in range(graph.v):
            if graph.edges[current_vertex][neighbor] != -1:#if connected edge
                distance = graph.edges[current_vertex][neighbor] 
                if neighbor not in graph.visited:
                    old_cost = D[neighbor]
                    new_cost = D[current_vertex] + distance
 
                    if new_cost < old_cost:
                        pq.put((new_cost, neighbor))
                        D[neighbor] = new_cost
    return D

'''

import heapq
class Solution:

    #Function to find the shortest distance of all the vertices
    #from the source vertex S.
    def dijkstra(self, V, adj, S):
        #code here
        
        l=[]*(V+1)
        dis=[float('inf')]*(V)
        dis[S]=0
        heapq.heappush(l,(0,S))
        
        while l:
            di,curr= heapq.heappop(l)
            
            for i in adj[curr]:
                nextdis=i[1]
                nextcurr=i[0]
                if di+nextdis<dis[nextcurr]:
                    dis[nextcurr]=di+nextdis
                    heapq.heappush(l,(dis[nextcurr],nextcurr))
                
        return dis

#{ 
#  Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys


if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        V,E = map(int,input().strip().split())
        adj = [[] for i in range(V)]
        for i in range(E):
            u,v,w = map(int,input().strip().split())
            adj[u].append([v,w])
            adj[v].append([u,w])
        S=int(input())
        ob = Solution()
        
        res = ob.dijkstra(V,adj,S)
        for i in res:
            print(i,end=" ")
        print()
'''