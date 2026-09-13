# Question: 
# 1. Minimax algo for 3 level game tree, 2 players.



# Code:
def minimax(depth, node_index, is_maximizing_player, leaf_values):
    # Base case: reached leaf nodes at depth 3
    if depth == 3:
        return leaf_values[node_index]

    if is_maximizing_player:
        best_eval = float('-inf')
        # Two branches per node
        for i in range(2):
            eval_score = minimax(depth + 1, node_index * 2 + i, False, leaf_values)
            best_eval = max(best_eval, eval_score)
        return best_eval
    else:
        best_eval = float('inf')
        # Two branches per node
        for i in range(2):
            eval_score = minimax(depth + 1, node_index * 2 + i, True, leaf_values)
            best_eval = min(best_eval, eval_score)
        return best_eval

# 8 leaf values for a binary tree of depth 3 (2^3 = 8 outcomes)
leaf_values = [3, 5, 2, 9, 12, 5, 23, 23]

optimal_value = minimax(depth=0, node_index=0, is_maximizing_player=True, leaf_values=leaf_values)
print("Optimal Score for Maximizing Player:", optimal_value)



# Output:
# Optimal Score for Maximizing Player: 12