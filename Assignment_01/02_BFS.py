# Question: 
# 2. Write a program to implement Breadth First search using python.



# Code:
from collections import deque

def bfs(graph, start_node):
    visited = set([start_node])
    queue = deque([start_node])
    traversal_order = []

    while queue:
        node = queue.popleft()
        traversal_order.append(node)

        for neighbor in graph.get(node, []):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
                
    return traversal_order

# Example Graph (Adjacency List)
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': [],
    'F': []
}

print("BFS Traversal:", bfs(graph, 'A'))



# Output:
# BFS Traversal: ['A', 'B', 'C', 'D', 'E', 'F']