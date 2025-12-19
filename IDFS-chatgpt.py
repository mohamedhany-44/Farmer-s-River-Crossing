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

    return [s for s in moves if is_valid(s)]

# Depth-Limited DFS
def dls(state, goal, depth, visited, path):
    if depth < 0:
        return False
    if state in visited:
        return False
    visited.add(state)
    path.append(state)
    if state == goal:
        return True
    for next_state in get_next_states(state):
        if dls(next_state, goal, depth - 1, visited, path):
            return True
    path.pop()
    return False

# Iterative Deepening DFS
def iddfs(start, goal, max_depth=20):
    for depth in range(max_depth + 1):
        visited = set()
        path = []
        if dls(start, goal, depth, visited, path):
            return path
    return None

def print_solution(path):
    print("IDFS Solution:")
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

# Initial and Goal states
start = (0, 0, 0, 0)
goal = (1, 1, 1, 1)

path = iddfs(start, goal)
print_solution(path)
