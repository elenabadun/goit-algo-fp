import uuid
import heapq
from collections import deque
import networkx as nx
import matplotlib.pyplot as plt


class Node:
    def __init__(self, key, color="skyblue"):
        self.left = None
        self.right = None
        self.val = key
        self.color = color
        self.id = str(uuid.uuid4())


def add_edges(graph, node, pos, x=0, y=0, layer=1):
    if node is not None:
        graph.add_node(node.id, color=node.color, label=node.val)
        if node.left:
            graph.add_edge(node.id, node.left.id)
            l = x - 1 / 2**layer
            pos[node.left.id] = (l, y - 1)
            add_edges(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1)
        if node.right:
            graph.add_edge(node.id, node.right.id)
            r = x + 1 / 2**layer
            pos[node.right.id] = (r, y - 1)
            add_edges(graph, node.right, pos, x=r, y=y - 1, layer=layer + 1)
    return graph


def draw_tree(tree_root, colors, title="Binary Tree"):
    tree = nx.DiGraph()
    pos = {tree_root.id: (0, 0)}
    tree = add_edges(tree, tree_root, pos)

    node_colors = [colors.get(node, "skyblue") for node in tree.nodes()]
    labels = {node[0]: node[1]["label"] for node in tree.nodes(data=True)}

    plt.figure(figsize=(10, 6))
    plt.title(title)
    nx.draw(
        tree,
        pos=pos,
        labels=labels,
        arrows=False,
        node_size=2500,
        node_color=node_colors,
    )
    plt.show()


def build_heap_tree(heap, index=0):
    if index >= len(heap):
        return None

    node = Node(heap[index])
    node.left = build_heap_tree(heap, 2 * index + 1)
    node.right = build_heap_tree(heap, 2 * index + 2)
    return node


def generate_color(step, total_steps):
    base_color = [0x00, 0xCC, 0x33]
    darken_factor = 0.5 + 0.5 * (1 - step / total_steps)
    new_color = [int(c * darken_factor) for c in base_color]
    return f"#{new_color[0]:02x}{new_color[1]:02x}{new_color[2]:02x}"


def dfs_visualize(root, total_steps):
    visited = set()
    stack = [root]
    colors = {}
    step = 0

    while stack:
        node = stack.pop()
        if node and node.id not in visited:
            visited.add(node.id)
            color = generate_color(step, total_steps)
            colors[node.id] = color
            step += 1
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
    return colors


def bfs_visualize(root, total_steps=1):
    visited = set()
    queue = deque([root])
    colors = {}
    step = 0

    while queue:
        node = queue.popleft()
        if node and node.id not in visited:
            visited.add(node.id)
            color = generate_color(step, total_steps)
            colors[node.id] = color
            step += 1
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
    return colors


def count_nodes(node):
    if node is None:
        return 0
    return 1 + count_nodes(node.left) + count_nodes(node.right)


if __name__ == "__main__":
    heap_list = [1, 3, 5, 7, 9, 2, 4, 34, 2, 1, 2]
    heapq.heapify(heap_list)

    heap_tree_root = build_heap_tree(heap_list)
    total_steps = count_nodes(heap_tree_root)

    # DFS visualization:
    dfs_colors = dfs_visualize(heap_tree_root, total_steps)
    draw_tree(heap_tree_root, dfs_colors, title="DFS visualization")

    # BFS visualization:
    bfs_colors = bfs_visualize(heap_tree_root, total_steps)
    draw_tree(heap_tree_root, bfs_colors, title="BFS visualization")
