import heapq

class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v, weight):
        if u not in self.graph:
            self.graph[u] = []
        if v not in self.graph:
            self.graph[v] = []
        self.graph[u].append((v, weight))
        self.graph[v].append((u, weight)) 

def dijkstra(graph, start):
    distances = {vertex: float('infinity') for vertex in graph.graph}
    distances[start] = 0

    priority_queue = [(0, start)]  
    
    while priority_queue:
        current_distance, current_vertex = heapq.heappop(priority_queue)

        if current_distance > distances[current_vertex]:
            continue

        for neighbor, weight in graph.graph.get(current_vertex, []):
            distance = current_distance + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))
    
    return distances

def main():
    g = Graph()
    g.add_edge('A', 'B', 1)
    g.add_edge('A', 'C', 4)
    g.add_edge('B', 'C', 2)
    g.add_edge('B', 'D', 5)
    g.add_edge('C', 'D', 1)

    start_vertex = 'A'
    shortest_paths = dijkstra(g, start_vertex)
    
    print(f"Найкоротші шляхи від {start_vertex}:")
    for vertex, distance in shortest_paths.items():
        print(f"Вершина {vertex}: {distance}")

if __name__ == "__main__":
    main()
