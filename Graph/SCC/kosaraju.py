# Kosaraju's algorithm to find strongly connected components in Python


from collections import defaultdict

class Graph:

    def __init__(self, vertex):
        self.V = vertex
        self.graph = defaultdict(list)

    # Add edge into the graph
    def add_edge(self, s, d):
        self.graph[s].append(d)

    # dfs
    def dfs(self, d, visited_vertex):
        visited_vertex[d] = True
        print(d, end='')
        for i in self.graph[d]:
            if not visited_vertex[i]:
                self.dfs(i, visited_vertex)

    def fill_order(self, d, visited_vertex, stack):
        visited_vertex[d] = True
        for i in self.graph[d]:
            if not visited_vertex[i]:
                self.fill_order(i, visited_vertex, stack)
        stack = stack.append(d)

    # transpose the matrix
    def transpose(self):
        g = Graph(self.V)

        for i in self.graph:
            for j in self.graph[i]:
                g.add_edge(j, i)
        return g

    # Print stongly connected components
    def print_scc(self):
        stack = []
        visited_vertex = [False] * (self.V)

        for i in range(self.V):
            if not visited_vertex[i]:
                self.fill_order(i, visited_vertex, stack)

        gr = self.transpose()

        visited_vertex = [False] * (self.V)

        while stack:
            i = stack.pop()
            if not visited_vertex[i]:
                gr.dfs(i, visited_vertex)
                print("")


g = Graph(8)
g.add_edge(0, 1)
g.add_edge(1, 2)
g.add_edge(2, 3)
g.add_edge(2, 4)
g.add_edge(3, 0)
g.add_edge(4, 5)
g.add_edge(5, 6)
g.add_edge(6, 4)
g.add_edge(6, 7)

print("Strongly Connected Components:")
g.print_scc()




# auroshisray
# 4 months ago

# PYTHON SOLUTION

# class Solution:
   
#    #Function to find number of strongly connected components in the graph.
#    def kosaraju(self, V, adj):
#        # code here
#        new_adj = [[] for _ in range(V)]
#        visited = [False for _ in range(V)]
#        stack = list()
#        # print(adj)
#        def topolike_dfs(node):
#            visited[node] = True
           
           
#            for adj_node in adj[node]:
#                if not visited[adj_node]:
#                    topolike_dfs(adj_node)
           
#            stack.append(node)
       
       
#        def transpose():
#            for node_index in range(V):
#                for adj_node in adj[node_index]:
#                    new_adj[adj_node].append(node_index)
#                visited[node_index] = False
#            # print(new_adj)
       
#        def revdfs(node):
#            visited[node] = True
           
#            for adj_node in new_adj[node]:
#                if not visited[adj_node]:
#                    revdfs(adj_node)
       
       
#        # driver section
#        for node in range(V):
#            if not visited[node]:
#                topolike_dfs(node)
               
#        transpose()
#        # print(stack)
#        count = 0
#        while stack:
#            node = stack.pop()
#            # print(node)
#            if not visited[node]:
#                count += 1
#                revdfs(node)
#                # count += 1
               
#        return count