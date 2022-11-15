'''
Dijkstra's Algorithm:

Finds the shortest path between two vertices on a graph

USE CASES
    1. GPS - Finding fastest route
    2. Network Routing - finds open shortest path for data
    3. Biology - used to model the spread of viruses among humans
    4. Airline tickets - finding cheapest route to your destination
    5. etc...

'''


class PriorityQueue:
    def __init__(self) -> None:
        self.values = []

    
    def enqueue(self, val, priority):
        self.values.append({'val': val, 'priority': priority})
        self.sort()

    
    def dequeue(self):
        return self.values.pop(0)


    def sort(self):
        self.values.sort(key=lambda i : i['priority'], reverse=False)



class WeightedGraph:

    def __init__(self) -> None:
        self.adjacency_list = {}


    def add_vertex(self, vertex):
        if not vertex in self.adjacency_list:
            self.adjacency_list[vertex] = []


    def add_edge(self, vertex1, vertex2, weight):
        self.adjacency_list[vertex1].append({ 'node': vertex2, 'weight': weight })
        self.adjacency_list[vertex2].append({ 'node': vertex1, 'weight': weight })


    def dijkstra(self, start_vertex, end_vertex):
        nodes = PriorityQueue()
        distances = {}
        previous = {}
        path = []
        smallest = None

        for vertex in self.adjacency_list:
            distances[vertex] = 0 if vertex == start_vertex else float('inf')
            nodes.enqueue(vertex, 0 if vertex == start_vertex else float('inf'))
            previous[vertex] = None

        while len(nodes.values):
            smallest = nodes.dequeue()['val']
            if smallest == end_vertex:
                while previous[smallest]:
                    path.append(smallest)
                    smallest = previous[smallest]
                break

            if smallest or distances[smallest] != float('inf'):
                for neighbor, _ in enumerate(self.adjacency_list[smallest]):
                    next_node = self.adjacency_list[smallest][neighbor]
                    candidate = distances[smallest] + next_node['weight']
                    next_neighbor =  next_node['node']

                    if candidate < distances[next_neighbor]:
                        distances[next_neighbor] = candidate
                        previous[next_neighbor] = smallest
                        nodes.enqueue(next_neighbor, candidate)

        path.append(smallest)
        return list(reversed(path))


wg = WeightedGraph()
wg.add_vertex('A')
wg.add_vertex('B')
wg.add_vertex('C')
wg.add_vertex('D')
wg.add_vertex('E')
wg.add_vertex('F')

wg.add_edge('A', 'B', 4)
wg.add_edge('A', 'C', 2)
wg.add_edge('B', 'E', 3)
wg.add_edge('C', 'D', 2)
wg.add_edge('C', 'F', 4)
wg.add_edge('D', 'E', 3)
wg.add_edge('D', 'F', 1)
wg.add_edge('E', 'F', 1)

print(wg.dijkstra('A', 'E'))