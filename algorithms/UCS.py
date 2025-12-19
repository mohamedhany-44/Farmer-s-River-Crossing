import heapq

# 0 = Left, 1 = Right
START = (0, 0, 0, 0)
GOAL = (1, 1, 1, 1)

# Check if state is safe
def valid(s):
    F, X, G, C = s
    if X == G and F != X:  # Fox eats Goat
        return False
    if G == C and F != G:  # Goat eats Cabbage
        return False
    return True

# Generate next states
def successors(s):
    F, X, G, C = s
    moves = []

    for name, ns in [
        ("Farmer alone", (1-F, X, G, C)),
        ("Farmer + Fox", (1-F, 1-X, G, C)) if F == X else None,
        ("Farmer + Goat", (1-F, X, 1-G, C)) if F == G else None,
        ("Farmer + Cabbage", (1-F, X, G, 1-C)) if F == C else None
    ]:
        if ns and valid(ns):
            moves.append((name, ns))

    return moves

# Uniform Cost Search
def UCS():
    pq = [(0, START, [])]
    visited = set()

    while pq:
        cost, state, path = heapq.heappop(pq)

        if state in visited:
            continue
        visited.add(state)

        if state == GOAL:
            return cost, path + [(state, "Goal")]

        for action, next_state in successors(state):
            heapq.heappush(pq, (cost + 1, next_state, path + [(state, action)]))

    return None

# Run
result = UCS()

if result:
    cost, path = result
    print("Minimum crossings:", cost, "\n")
    for i, (state, action) in enumerate(path, 1):
        print(f"{i}. {action} -> {state}")
else:
    print("No solution")
