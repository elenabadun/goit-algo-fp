import networkx as nx
import matplotlib.pyplot as plt
import heapq

# Створення графа:
G = nx.Graph()
G.add_edge("A", "B", weight=5)
G.add_edge("A", "C", weight=10)
G.add_edge("B", "D", weight=3)
G.add_edge("C", "D", weight=2)
G.add_edge("D", "E", weight=4)


# Реалізація алгоритму Дейкстри:
def dijkstra(graph, start):

    shortest_paths = {vertex: float("infinity") for vertex in graph.nodes}
    shortest_paths[start] = 0

    # Бінарна купа:
    priority_queue = [(0, start)]

    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)

        for neighbor in graph.neighbors(current_node):
            weight = graph[current_node][neighbor]["weight"]
            distance = current_distance + weight

            if distance < shortest_paths[neighbor]:
                shortest_paths[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return shortest_paths


shortest_paths = dijkstra(G, "A")

print(f"Найкоротший шлях від вершини A: {shortest_paths}")

# Візуалізація графа:
pos = nx.spring_layout(G, seed=42)
nx.draw_networkx_nodes(G, pos, node_size=700, node_color="lightblue")
nx.draw_networkx_edges(G, pos, width=2)
nx.draw_networkx_labels(G, pos, font_size=14, font_family="sans-serif")

edge_labels = nx.get_edge_attributes(G, "weight")
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)

plt.axis("off")
plt.show()
