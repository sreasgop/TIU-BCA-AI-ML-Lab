# Question:
# 1. Implement A* algorithm  to find the shortest path in 4x4 grid.



# Code:
import heapq

def a_star_grid(grid, start, goal):
    rows, cols = len(grid), len(grid[0])
    
    def heuristic(point):
        return abs(point[0] - goal[0]) + abs(point[1] - goal[1])

    # Priority Queue stores (f_score, g_score, current_node, path)
    open_set = [(heuristic(start), 0, start, [start])]
    visited = {}

    while open_set:
        f, g, current, path = heapq.heappop(open_set)

        if current == goal:
            return path

        if current in visited and visited[current] <= g:
            continue
        visited[current] = g

        r, c = current
        # Up, Down, Left, Right moves
        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 0:
                neighbor = (nr, nc)
                new_g = g + 1
                new_f = new_g + heuristic(neighbor)
                heapq.heappush(open_set, (new_f, new_g, neighbor, path + [neighbor]))

    return None

# 4x4 Grid (0 = Open Path, 1 = Wall)
grid_4x4 = [
    [0, 0, 0, 0],
    [1, 1, 0, 1],
    [0, 0, 0, 0],
    [0, 1, 1, 0]
]

path = a_star_grid(grid_4x4, start=(0, 0), goal=(3, 3))
print("A* Shortest Path:", path)



# Output:
# A* Shortest Path: [(0, 0), (0, 1), (0, 2), (1, 2), (2, 2), (2, 3), (3, 3)]