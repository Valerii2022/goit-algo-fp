import uuid
import networkx as nx
import matplotlib.pyplot as plt
from collections import deque

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
            l = x - 1 / 2 ** layer
            pos[node.left.id] = (l, y - 1)
            l = add_edges(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1)
        if node.right:
            graph.add_edge(node.id, node.right.id)
            r = x + 1 / 2 ** layer
            pos[node.right.id] = (r, y - 1)
            r = add_edges(graph, node.right, pos, x=r, y=y - 1, layer=layer + 1)
    return graph

def generate_color(order, total):
    base_r = 18
    base_g = 150
    base_b = 240

    brightness = int(255 * (order / total))
    
    r = min(255, base_r + brightness)
    g = min(255, base_g + brightness)
    b = min(255, base_b + brightness)

    color = f"#{r:02X}{g:02X}{b:02X}"
    return color

def visualize_tree(tree_root, traversal_order, title):
    tree = nx.DiGraph()
    pos = {tree_root.id: (0, 0)}
    tree = add_edges(tree, tree_root, pos)

    colors = [generate_color(i, len(traversal_order)) for i in range(len(traversal_order))]
    node_colors = {node.id: colors[i] for i, node in enumerate(traversal_order)}

    labels = {node[0]: node[1]['label'] for node in tree.nodes(data=True)}

    plt.figure(figsize=(8, 5))
    nx.draw(tree, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=[node_colors.get(n, "#1296F0") for n in tree.nodes()])
    plt.title(title)
    plt.show()

def dfs(tree_root):
    stack = [tree_root]
    visited = []
    while stack:
        node = stack.pop()
        if node:
            visited.append(node)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
    return visited

def bfs(tree_root):
    queue = deque([tree_root])
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

if __name__ == "__main__":

    # Приклад використання
    root = Node(0)
    root.left = Node(4)
    root.left.left = Node(5)
    root.left.right = Node(10)
    root.right = Node(1)
    root.right.left = Node(3)

    # DFS та BFS
    dfs_order = dfs(root)
    bfs_order = bfs(root)

    # Візуалізація
    visualize_tree(root, dfs_order, "DFS Traversal")
    visualize_tree(root, bfs_order, "BFS Traversal")


