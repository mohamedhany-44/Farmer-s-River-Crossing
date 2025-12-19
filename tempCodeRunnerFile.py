from collections import deque
import time

# State: (Farmer, Fox, Goat, Cabbage)
# 0 = Left bank, 1 = Right bank
items = ["Farmer", "Fox", "Goat", "Cabbage"]

def is_valid(state):
    F, X, G, C = state
    # Fox with Goat without Farmer
    if X == G and F != X:
        return False
    # Goat with Cabbage without Farmer
    if G == C and F != G:
        return False
    return True

def get_next_states(state):
    F, X, G, C = state
    moves = []
    # Farmer moves alone
    moves.append((1 - F, X, G, C))
    # Farmer moves with Fox
    if F == X:
        moves.append((1 - F, 1 - X, G, C))
    # Farmer moves with Goat
    if F == G:
        moves.append((1 - F, X, 1 - G, C))
    # Farmer moves with Cabbage
    if F == C:
        moves.append((1 - F, X, G, 1 - C))
    # Keep only valid states
    return [s for s in moves if is_valid(s)]

def bfs(start, goal):
    visited = set()
    queue = deque()
    queue.append((start, [start]))  # (state, path)
    nodes_expanded = 0

    while queue:
        state, path = queue.popleft()
        nodes_expanded += 1

        if state == goal:
            return path, nodes_expanded

        if state in visited:
            continue

        visited.add(state)

        for next_state in get_next_states(state):
            if next_state not in visited:
                queue.append((next_state, path + [next_state]))

    return None, nodes_expanded

def print_solution(path):
    print("BFS Solution:")
    print("=======================")

    for i, state in enumerate(path):
        left = []
        right = []

        for idx, pos in enumerate(state):
            if pos == 0:
                left.append(items[idx])
            else:
                right.append(items[idx])

        print(f"Step {i}:")
        print("Left bank:", ", ".join(left) if left else "Empty")
        print("Right bank:", ", ".join(right) if right else "Empty")
        print()

    print(f"Total steps: {len(path) - 1}")

# ------------------- RUN -------------------
start_state = (0, 0, 0, 0)
goal_state = (1, 1, 1, 1)

start_time = time.time()
path, nodes_expanded = bfs(start_state, goal_state)
end_time = time.time()

if path:
    print_solution(path)
    print(f"Nodes expanded: {nodes_expanded}")
    print(f"Time taken: {end_time - start_time:.6f} seconds")
else:
    print("No solution found.")
