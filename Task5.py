import uuid
import networkx as nx
import matplotlib.pyplot as plt

from collections import deque


class Node:
    def __init__(self, key, color="#1296F0"):
        self.left = None
        self.right = None
        self.val = key
        self.color = color
        self.id = str(uuid.uuid4())


# Додавання ребер
def add_edges(graph, node, pos, x=0, y=0, layer=1):

    if node is not None:

        graph.add_node(
            node.id,
            color=node.color,
            label=node.val
        )

        if node.left:

            graph.add_edge(node.id, node.left.id)

            left_x = x - 1 / 2 ** layer

            pos[node.left.id] = (left_x, y - 1)

            add_edges(
                graph,
                node.left,
                pos,
                x=left_x,
                y=y - 1,
                layer=layer + 1
            )

        if node.right:

            graph.add_edge(node.id, node.right.id)

            right_x = x + 1 / 2 ** layer

            pos[node.right.id] = (right_x, y - 1)

            add_edges(
                graph,
                node.right,
                pos,
                x=right_x,
                y=y - 1,
                layer=layer + 1
            )

    return graph


# Малювання дерева
def draw_tree(tree_root):

    tree = nx.DiGraph()

    pos = {tree_root.id: (0, 0)}

    add_edges(tree, tree_root, pos)

    colors = [
        node[1]["color"]
        for node in tree.nodes(data=True)
    ]

    labels = {
        node[0]: node[1]["label"]
        for node in tree.nodes(data=True)
    }

    plt.figure(figsize=(8, 5))

    nx.draw(
        tree,
        pos=pos,
        labels=labels,
        arrows=False,
        node_size=2500,
        node_color=colors
    )

    plt.show()


# Генерація кольору
def generate_color(step, total_steps):

    intensity = int(255 * (step / total_steps))

    hex_intensity = format(intensity, '02x')

    return f"#{hex_intensity}{hex_intensity}FF"


# DFS — обхід у глибину
def dfs(root):

    stack = [root]

    visited = []

    while stack:

        node = stack.pop()

        if node:

            visited.append(node)

            # Спочатку right, потім left
            if node.right:
                stack.append(node.right)

            if node.left:
                stack.append(node.left)

    return visited


# BFS — обхід у ширину
def bfs(root):

    queue = deque([root])

    visited = []

    while queue:

        node = queue.popleft()

        if node:

            visited.append(node)

            if node.left:
                queue.append(node.left)

            if node.right:
                queue.append(node.right)

    return visited


# Фарбування вузлів
def color_nodes(nodes):

    total = len(nodes)

    for index, node in enumerate(nodes):
        node.color = generate_color(index + 1, total)


def main():

    # Створення дерева
    root = Node(0)

    root.left = Node(4)
    root.right = Node(1)

    root.left.left = Node(5)
    root.left.right = Node(10)

    root.right.left = Node(3)

    # DFS
    print("DFS (обхід у глибину):")

    dfs_nodes = dfs(root)

    for node in dfs_nodes:
        print(node.val, end=" ")

    print("\n")

    color_nodes(dfs_nodes)

    draw_tree(root)

    # Скидання кольорів
    for node in dfs_nodes:
        node.color = "#1296F0"

    # BFS
    print("BFS (обхід у ширину):")

    bfs_nodes = bfs(root)

    for node in bfs_nodes:
        print(node.val, end=" ")

    print("\n")

    color_nodes(bfs_nodes)

    draw_tree(root)


if __name__ == "__main__":
    main()