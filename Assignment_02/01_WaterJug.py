# Question:
# 1. Solve water jug problem using best first search 



# Code:
import heapq

def best_first_search_water_jug(jug1_cap, jug2_cap, target):
    # State representation: (jug1, jug2)
    start_state = (0, 0)
    
    # Heuristic: Absolute difference from target to nearest jug's current level
    def heuristic(state):
        j1, j2 = state
        return min(abs(target - j1), abs(target - j2))

    # Priority queue stores (heuristic_value, path_of_states)
    pq = [(heuristic(start_state), [start_state])]
    visited = set([start_state])

    while pq:
        _, path = heapq.heappop(pq)
        current = path[-1]
        j1, j2 = current

        if j1 == target or j2 == target:
            return path

        # Generate all possible successor states
        next_states = [
            (jug1_cap, j2),  # Fill Jug 1
            (j1, jug2_cap),  # Fill Jug 2
            (0, j2),         # Empty Jug 1
            (j1, 0),         # Empty Jug 2
            # Pour Jug 1 -> Jug 2
            (j1 - min(j1, jug2_cap - j2), j2 + min(j1, jug2_cap - j2)),
            # Pour Jug 2 -> Jug 1
            (j1 + min(j2, jug1_cap - j1), j2 - min(j2, jug1_cap - j1))
        ]

        for state in next_states:
            if state not in visited:
                visited.add(state)
                heapq.heappush(pq, (heuristic(state), path + [state]))

    return None

# Example Usage: Jug 1 = 4L, Jug 2 = 3L, Target = 2L
solution = best_first_search_water_jug(4, 3, 2)
print("Water Jug Solution Path:")
for step in solution:
    print(step)



# Output:
# Water Jug Solution Path:
# (0, 0)
# (0, 3)
# (3, 0)
# (3, 3)
# (4, 2)