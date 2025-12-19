from collections import deque
import time

# State: (Farmer, Fox, Goat, Cabbage)
# 0 = Left bank, 1 = Right bank
items = ["Farmer", "Fox", "Goat", "Cabbage"]

def is_valid(state):
    F, X, G, C = state
    if X == G and F != X:
        return False
    if G == C and F != G:
        return False
    return True

def get_next_states_with_move(state):
    F, X, G, C = state
    moves = []

    # Farmer moves alone
    new_state = (1 - F, X, G, C)
    if is_valid(new_state):
        moves.append((new_state, "Farmer"))

    # Farmer moves with Fox
    if F == X:
        new_state = (1 - F, 1 - X, G, C)
        if is_valid(new_state):
            moves.append((new_state, "Farmer + Fox"))

    # Farmer moves with Goat
    if F == G:
        new_state = (1 - F, X, 1 - G, C)
        if is_valid(new_state):
            moves.append((new_state, "Farmer + Goat"))

    # Farmer moves with Cabbage
    if F == C:
        new_state = (1 - F, X, G, 1 - C)
        if is_valid(new_state):
            moves.append((new_state, "Farmer + Cabbage"))

    return moves

def bfs(start, goal):
    visited = set()
    queue = deque()
    queue.append((start, [start], []))  # (state, path, moves)
    nodes_expanded = 0

    while queue:
        state, path, moves = queue.popleft()
        nodes_expanded += 1

        if state == goal:
            return path, moves, nodes_expanded

        if state in visited:
            continue

        visited.add(state)

        for next_state, move_desc in get_next_states_with_move(state):
            if next_state not in visited:
                queue.append(
                    (next_state, path + [next_state], moves + [move_desc])
                )

    return None, None, nodes_expanded

def print_solution(path, moves):
    print("BFS Solution:")
    print("=======================")

    for i, state in enumerate(path):
        left, right = [], []

        for idx, pos in enumerate(state):
            if pos == 0:
                left.append(items[idx])
            else:
                right.append(items[idx])

        if i == 0:
            print("Step 0: Start")
        else:
            direction = "Right Bank" if state[0] == 1 else "Left Bank"
            print(f"Step {i}: {moves[i-1]} → {direction}")

        print("Left bank:", ", ".join(left) if left else "Empty")
        print("Right bank:", ", ".join(right) if right else "Empty")
        print()

    print(f"Total steps: {len(path) - 1}")

# ------------------- RUN -------------------
start_state = (0, 0, 0, 0)
goal_state = (1, 1, 1, 1)

start_time = time.time()
path, moves, nodes_expanded = bfs(start_state, goal_state)
end_time = time.time()

if path:
    print_solution(path, moves)
    print(f"Nodes expanded: {nodes_expanded}")
    print(f"Time taken: {end_time - start_time:.6f} seconds")
else:
    print("No solution found.")
