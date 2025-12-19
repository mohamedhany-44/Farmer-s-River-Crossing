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

def get_next_states_with_move(state):
    """Return list of (next_state, move_description)"""
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

def dls(state, goal, depth, visited, path, moves_path, nodes_expanded):
    nodes_expanded[0] += 1
    if depth < 0 or state in visited:
        return False
    visited.add(state)
    path.append(state)

    if state == goal:
        return True

    for next_state, move_desc in get_next_states_with_move(state):
        if dls(next_state, goal, depth - 1, visited, path, moves_path, nodes_expanded):
            moves_path.append(move_desc)
            return True

    path.pop()
    return False

def iddfs(start, goal, max_depth=20):
    total_nodes_expanded = 0
    start_time = time.time()
    for depth in range(max_depth + 1):
        visited = set()
        path = []
        moves_path = []
        nodes_expanded = [0]
        if dls(start, goal, depth, visited, path, moves_path, nodes_expanded):
            end_time = time.time()
            moves_path.reverse()  # reverse to match step order
            return path, moves_path, nodes_expanded[0], end_time - start_time
        total_nodes_expanded += nodes_expanded[0]
    end_time = time.time()
    return None, [], total_nodes_expanded, end_time - start_time

def print_solution(path, moves):
    print("IDDFS Solution:")
    print("=======================")
    for i, state in enumerate(path):
        left = []
        right = []
        for idx, pos in enumerate(state):
            if pos == 0:
                left.append(items[idx])
            else:
                right.append(items[idx])
        move_text = moves[i-1] + " → " + ("Right Bank" if state[0]==1 else "Left Bank") if i > 0 else "Start"
        print(f"Step {i}: Move: {move_text}")
        print("Left bank:", ", ".join(left) if left else "Empty")
        print("Right bank:", ", ".join(right) if right else "Empty")
        print()
    print(f"Total steps: {len(path) - 1}")

# ------------------- RUN -------------------
start_state = (0, 0, 0, 0)
goal_state = (1, 1, 1, 1)

path, moves, nodes_expanded, time_taken = iddfs(start_state, goal_state)

if path:
    print_solution(path, moves)
    print(f"Nodes expanded: {nodes_expanded}")
    print(f"Time taken: {time_taken:.6f} seconds")
else:
    print("No solution found.")
