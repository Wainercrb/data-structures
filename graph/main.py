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

Adjacency Matrix Vs Big O:
'''


class Graph():
    '''Undirect Graph'''    

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
        

g = Graph()
g.add_vertex('Dallas')
g.add_vertex('Tokyo')
g.add_vertex('Aspen')
g.add_vertex("Los Angeles");
g.add_vertex("Hong Kong")
g.add_edge('Dallas', 'Tokyo')
g.add_edge('Dallas', 'Aspen')
g.add_edge("Hong Kong", "Tokyo");
g.add_edge("Hong Kong", "Dallas");
g.add_edge("Los Angeles", "Hong Kong");
g.add_edge("Los Angeles", "Aspen");
print('add vertex && edges', g.adjacency_list, end='\n')
g.remove_edge('Dallas', 'Aspen')
g.remove_edge('Dallas', 'Tokyo')
print('remove edge', g.adjacency_list, end='\n')
print('remove vertex before', g.adjacency_list, end='\n')
g.remove_vertex('Hong Kong')
print('remove vertex after', g.adjacency_list, end='\n')



