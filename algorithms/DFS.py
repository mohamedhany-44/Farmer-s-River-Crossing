import time

# State: (Farmer, Fox, Goat, Cabbage)
items = ["Farmer", "Fox", "Goat", "Cabbage"]

def is_valid(state):
    F, X, G, C = state
    if X == G and F != X:
        return False
    if G == C and F != G:
        return False
    return True

def get_next_states(state):
    F, X, G, C = state
    moves = []
    moves.append((1 - F, X, G, C))
    if F == X:
        moves.append((1 - F, 1 - X, G, C))
    if F == G:
        moves.append((1 - F, X, 1 - G, C))
    if F == C:
        moves.append((1 - F, X, G, 1 - C))
    return [s for s in moves if is_valid(s)]

# DFS
def dfs(state, goal, visited, path, nodes_expanded):
    nodes_expanded[0] += 1
    if state in visited:
        return False

    visited.add(state)
    path.append(state)

    if state == goal:
        return True

    for next_state in get_next_states(state):
        if dfs(next_state, goal, visited, path, nodes_expanded):
            return True

    path.pop()
    return False

# ✅ THIS IS WHAT YOU WANTED
def print_solution_with_moves(path, nodes_expanded, time_taken):
    print("DFS Solution")
    print("==============================")

    for i in range(1, len(path)):
        prev = path[i - 1]
        curr = path[i]

        # Determine move
        moved = []
        for j in range(4):
            if prev[j] != curr[j]:
                moved.append(items[j])

        direction = "Right Bank" if curr[0] == 1 else "Left Bank"

        # Banks
        left = []
        right = []
        for idx, pos in enumerate(curr):
            if pos == 0:
                left.append(items[idx])
            else:
                right.append(items[idx])

        print(f"Step {i}: {' + '.join(moved)} > {direction}")
        print("Left bank:", ", ".join(left) if left else "Empty")
        print("Right bank:", ", ".join(right) if right else "Empty")
        print()

    print(f"Total steps: {len(path) - 1}")
    print(f"Nodes expanded: {nodes_expanded}")
    print(f"Time taken: {time_taken:.6f} seconds")

# ------------------- RUN -------------------
start_state = (0, 0, 0, 0)
goal_state = (1, 1, 1, 1)

visited = set()
path = []
nodes_expanded = [0]

start_time = time.time()
found = dfs(start_state, goal_state, visited, path, nodes_expanded)
end_time = time.time()

if found:
    print_solution_with_moves(path, nodes_expanded[0], end_time - start_time)
else:
    print("No solution found.")
