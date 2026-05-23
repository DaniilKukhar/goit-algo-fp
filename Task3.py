import heapq


class Graph:
    def __init__(self):
        self.graph = {}

    # Додавання ребра
    def add_edge(self, u, v, weight):

        if u not in self.graph:
            self.graph[u] = []

        if v not in self.graph:
            self.graph[v] = []

        self.graph[u].append((v, weight))
        self.graph[v].append((u, weight))

    # Алгоритм Дейкстри
    def dijkstra(self, start):

        # Відстані до всіх вершин
        distances = {
            vertex: float('inf')
            for vertex in self.graph
        }

        distances[start] = 0

        # Бінарна купа
        priority_queue = [(0, start)]

        while priority_queue:

            current_distance, current_vertex = heapq.heappop(priority_queue)

            # Пропуск застарілих значень
            if current_distance > distances[current_vertex]:
                continue

            # Перегляд сусідів
            for neighbor, weight in self.graph[current_vertex]:

                distance = current_distance + weight

                # Якщо знайдено коротший шлях
                if distance < distances[neighbor]:

                    distances[neighbor] = distance

                    heapq.heappush(
                        priority_queue,
                        (distance, neighbor)
                    )

        return distances


def main():

    graph = Graph()

    # Створення графа
    graph.add_edge("A", "B", 4)
    graph.add_edge("A", "C", 2)
    graph.add_edge("B", "C", 1)
    graph.add_edge("B", "D", 5)
    graph.add_edge("C", "D", 8)
    graph.add_edge("C", "E", 10)
    graph.add_edge("D", "E", 2)
    graph.add_edge("D", "F", 6)
    graph.add_edge("E", "F", 3)

    # Запуск алгоритму Дейкстри
    start_vertex = "A"

    shortest_paths = graph.dijkstra(start_vertex)

    print(f"Найкоротші шляхи від вершини {start_vertex}:")

    for vertex, distance in shortest_paths.items():
        print(f"{vertex}: {distance}")


if __name__ == "__main__":
    main()