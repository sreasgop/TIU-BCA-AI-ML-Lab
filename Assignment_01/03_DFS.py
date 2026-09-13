# Question:
# 3. Write a program to implement Depth First search using python.



# Code:
def dfs(graph, start_node, visited=None, traversal_order=None):
    if visited is None:
        visited = set()
    if traversal_order is None:
        traversal_order = []

    visited.add(start_node)
    traversal_order.append(start_node)

    for neighbor in graph.get(start_node, []):
        if neighbor not in visited:
            dfs(graph, neighbor, visited, traversal_order)
            
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

print("DFS Traversal:", dfs(graph, 'A'))



# Output:
# DFS Traversal: ['A', 'B', 'D', 'E', 'C', 'F']