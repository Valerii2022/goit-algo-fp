import heapq

class Graph:
    def __init__(self):
        self.edges = {}
    
    def add_edge(self, from_node, to_node, weight):
        if from_node not in self.edges:
            self.edges[from_node] = []
        if to_node not in self.edges:
            self.edges[to_node] = []
        self.edges[from_node].append((to_node, weight))
        self.edges[to_node].append((from_node, weight))

def dijkstra(graph, start):
    priority_queue = []
    heapq.heappush(priority_queue, (0, start))
    distances = {vertex: float('infinity') for vertex in graph.edges}
    distances[start] = 0
    visited = set()
    
    while priority_queue:
        current_distance, current_vertex = heapq.heappop(priority_queue)
        
        if current_vertex in visited:
            continue
        
        visited.add(current_vertex)
        
        for neighbor, weight in graph.edges[current_vertex]:
            distance = current_distance + weight
            
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))
    
    return distances

# Приклад використання:
graph = Graph()
graph.add_edge('A', 'B', 1)
graph.add_edge('A', 'C', 4)
graph.add_edge('B', 'C', 2)
graph.add_edge('B', 'D', 5)
graph.add_edge('C', 'D', 1)
graph.add_edge('D', 'E', 3)

start_vertex = 'A'
distances = dijkstra(graph, start_vertex)

print(f"Найкоротші відстані від вершини {start_vertex}:")
for vertex in distances:
    print(f"Відстань до вершини {vertex}: {distances[vertex]}")

