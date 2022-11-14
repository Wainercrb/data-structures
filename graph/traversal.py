'''Graph

Description: A data structure consists  of a finite (and possibly mutable) set
of vertices or nodes or points together with a set of unodered pairs of these 
vertices for an undirected graph or  a set of ordered pairs for a directed graph

Use Cases:

1. Social Networks 
2. Location / Mapping 
3. Routing Algorithms
4. Visual Hierarchy
5. File System Optimizations
6. More....

Keywords
1. Vertex - a node
2. Edge - connection between nodes
3. Weighted/Unweighted - values assigned to distaces between vertices
4. Directed/Undirected - directions assigned to distaced between vertices

Graph traversal

Use cases
1. Peer to peer networking
2. Web crawlers finding/recommendations
3. Shortest path problems
 1. GPS Navegation
 2. Solving mazes
 3. AI(shortest path to win the game)
'''


class Graph():
    '''Undirect Graph traversal'''    

    def __init__(self) -> None:
        self.adjacency_list = {}

    
    def add_vertex(self, name):
        
        if not name:
            return None

        if not name in self.adjacency_list:   
            self.adjacency_list[name] = [] 

        return self.adjacency_list[name]


    def add_edge(self, vertex1, vertex2):
        self.adjacency_list[vertex1].append(vertex2)
        self.adjacency_list[vertex2].append(vertex1)


    def remove_edge(self, vertex1, vertex2):
        clean_vertex1 = filter(lambda i: i != vertex2, self.adjacency_list[vertex1])
        clean_vertex2 = filter(lambda i: i != vertex1, self.adjacency_list[vertex2])

        self.adjacency_list[vertex1] = list(clean_vertex1)
        self.adjacency_list[vertex2] = list(clean_vertex2)


    def remove_vertex(self, vertex):
        while len(self.adjacency_list[vertex]):
            adjacent_vertex = self.adjacency_list[vertex][-1]
            self.remove_edge(vertex, adjacent_vertex)
        
        del self.adjacency_list[vertex] 


    def depth_first_recursive(self, start_vertex):
        result = []
        visited = {}
        adjacency_list = self.adjacency_list
        
        def dfs(vertex):
            if not vertex:
                return None
            visited[vertex] = True
            result.append(vertex)
            
            for i in adjacency_list[vertex]:
                if not i in visited:
                    return dfs(i)

        dfs(start_vertex) 

        return result

    def depth_first_iterative(self, start):
        stack = [start]
        result = []
        visited = {}
        curr_vertex = None

        visited[start] = True
        while len(stack):
            curr_vertex = stack.pop()
            result.append(curr_vertex)

            for neighbor in self.adjacency_list[curr_vertex]:
                if not neighbor in visited:
                    visited[neighbor] = True
                    stack.append(neighbor)

        return result


g = Graph()
g.add_vertex('A')
g.add_vertex('B')
g.add_vertex('C')
g.add_vertex('D');
g.add_vertex('E')
g.add_vertex('F')
g.add_edge('A', 'B')
g.add_edge('A', 'C')
g.add_edge('B', 'D');
g.add_edge('D', 'E');
g.add_edge('C', 'E');
g.add_edge('D', 'F');
g.add_edge('E', 'F');

#      A
#    /   \
#   B     C
#   \     |
#    D----E
#     \  |
#       F

g.depth_first_recursive('A')
print(g.depth_first_iterative('A'))