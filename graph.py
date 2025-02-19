import heapq

class Graph:
    def __init__(self):
        self.adj_list = {}
    
    def add_edge(self, u, v, weight):
        if u not in self.adj_list:
            self.adj_list[u] = []
        if v not in self.adj_list:
            self.adj_list[v] = []
        self.adj_list[u].append((v, weight))
        self.adj_list[v].append((u, weight))  
    
    def display_graph(self):
        print("\nGraph Representation (Adjacency List):")
        for node in self.adj_list:
            print(f"{node}: {self.adj_list[node]}")

    def dijkstra(self, start):
        shortest_paths = {node: float('inf') for node in self.adj_list}
        shortest_paths[start] = 0
        priority_queue = [(0, start)]

        while priority_queue:
            current_distance, current_node = heapq.heappop(priority_queue)

            if current_distance > shortest_paths[current_node]:
                continue

            for neighbor, weight in self.adj_list[current_node]:
                distance = current_distance + weight

                if distance < shortest_paths[neighbor]:
                    shortest_paths[neighbor] = distance
                    heapq.heappush(priority_queue, (distance, neighbor))

        return shortest_paths

print("\nDijkstra's Algorithm):")
city_graph = Graph()
city_graph.add_edge("A", "B", 4)
city_graph.add_edge("A", "C", 5)
city_graph.add_edge("B", "D", 9)
city_graph.add_edge("B", "C", 11)
city_graph.add_edge("C", "E", 3)
city_graph.add_edge("D", "E", 7)
city_graph.add_edge("D", "F", 2)
city_graph.add_edge("E", "F", 6)

city_graph.display_graph()

shortest_paths = city_graph.dijkstra("A")
print("\nShortest paths from A:", shortest_paths)
