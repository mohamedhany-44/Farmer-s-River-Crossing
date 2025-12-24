import heapq

# 0 = Left, 1 = Right
START = (0, 0, 0, 0)
GOAL = (1, 1, 1, 1)

# -----------------------------------
# Check if state is safe
# -----------------------------------
def valid(s):
    F, X, G, C = s
    if X == G and F != X:   # Fox eats Goat
        return False
    if G == C and F != G:   # Goat eats Cabbage
        return False
    return True

# -----------------------------------
# Generate next valid states
# -----------------------------------
def successors(s):
    F, X, G, C = s
    moves = []

    candidates = [
        ("Farmer alone", (1-F, X, G, C)),
        ("Farmer + Fox", (1-F, 1-X, G, C)) if F == X else None,
        ("Farmer + Goat", (1-F, X, 1-G, C)) if F == G else None,
        ("Farmer + Cabbage", (1-F, X, G, 1-C)) if F == C else None
    ]

    for item in candidates:
        if item:
            action, ns = item
            if valid(ns):
                moves.append((action, ns))

    return moves

# -----------------------------------
# Uniform Cost Search
# -----------------------------------
def UCS():
    pq = [(0, START, [START], [])]   # (cost, state, path, moves)
    visited = set()

    while pq:
        cost, state, path, moves = heapq.heappop(pq)

        if state in visited:
            continue
        visited.add(state)

        if state == GOAL:
            return cost, path, moves

        for action, next_state in successors(state):
            heapq.heappush(
                pq,
                (cost + 1, next_state, path + [next_state], moves + [action])
            )

    return None

# -----------------------------------
# Print state function similar to solver
# -----------------------------------
def print_state(state):
    """Display the current state visually"""
    items = ["Farmer", "Fox", "Goat", "Cabbage"]
    left_bank = []
    right_bank = []
    
    for i, item in enumerate(items):
        if state[i] == 0:
            left_bank.append(item)
        else:
            right_bank.append(item)
    
    print(f"Left Bank:  {', '.join(left_bank) if left_bank else 'Empty'}")
    print(f"Right Bank: {', '.join(right_bank) if right_bank else 'Empty'}")
    print("-" * 40)

# -----------------------------------
# Print solution like the solver
# -----------------------------------
def print_solution(path, moves, cost):
    """Display the complete solution with steps"""
    print(f"\n{'='*60}")
    print(f"UNIFORM COST SEARCH SOLUTION")
    print(f"{'='*60}")
    
    for i, state in enumerate(path):
        if i == 0:
            print(f"\nStep 0: Initial State")
        else:
            print(f"\nStep {i}: {moves[i-1]}")
        
        print_state(state)
    
    print(f"\nTotal steps: {len(path) - 1}")
    print(f"Total cost: {cost}")
    print(f"{'='*60}")

# -----------------------------------
# Run UCS with enhanced output
# -----------------------------------
print("="*80)
print("UNIFORM COST SEARCH FOR FARMER-FOX-GOAT-CABBAGE PUZZLE")
print("="*80)

result = UCS()

if result:
    cost, path, moves = result
    print_solution(path, moves, cost)
    
    # Also print the simple step-by-step format from original
    print("\n" + "="*60)
    print("STEP-BY-STEP SOLUTION")
    print("="*60)
    print(f"Minimum crossings: {cost}")
    for i, (action, state) in enumerate(zip(moves, path[1:]), 1):
        print(f"{i}. {action} -> {state}")
else:
    print("No solution found!")