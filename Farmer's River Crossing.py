from collections import deque

# Characters
FARMER, FOX, GOAT, CABBAGE = "farmer", "fox", "goat", "cabbage"
ALL_ITEMS = [FARMER, FOX, GOAT, CABBAGE]

# ---------------- GAME CHECKS ----------------

def is_valid(state):
    left, right = state
    for bank in [left, right]:
        if FARMER not in bank:
            if FOX in bank and GOAT in bank:
                return False
            if GOAT in bank and CABBAGE in bank:
                return False
    return True

def is_goal(state):
    left, right = state
    return len(left) == 0

# ---------------- HELPER FUNCTIONS ----------------

def get_possible_moves(state):
    left, right = state
    current_bank = left if FARMER in left else right
    other_bank = right if FARMER in left else left

    moves = []

    # Farmer moves alone
    new_current = set(current_bank)
    new_other = set(other_bank)
    new_current.remove(FARMER)
    new_other.add(FARMER)
    new_state = (frozenset(new_current), frozenset(new_other)) if FARMER in left else (frozenset(new_other), frozenset(new_current))
    if is_valid(new_state):
        moves.append((new_state, None))

    # Farmer moves with one item
    for item in current_bank:
        if item == FARMER:
            continue
        new_current = set(current_bank)
        new_other = set(other_bank)
        new_current.remove(FARMER)
        new_current.remove(item)
        new_other.add(FARMER)
        new_other.add(item)
        new_state = (frozenset(new_current), frozenset(new_other)) if FARMER in left else (frozenset(new_other), frozenset(new_current))
        if is_valid(new_state):
            moves.append((new_state, item))

    return moves

# ---------------- BFS SOLVER ----------------

def solve():
    initial_state = (frozenset(ALL_ITEMS), frozenset())
    queue = deque()
    queue.append((initial_state, []))
    visited = set()

    while queue:
        state, path = queue.popleft()
        if state in visited:
            continue
        visited.add(state)

        if is_goal(state):
            return path

        for next_state, move_item in get_possible_moves(state):
            queue.append((next_state, path + [move_item]))

# ---------------- RUN AUTOMATED GAME ----------------

def run_game():
    path = solve()
    if not path:
        print("No solution found.")
        return

    banks = [ALL_ITEMS.copy(), []]
    print("*" * 50)
    print("Farmer, Fox, Goat, and Cabbage - Auto Solver")
    print("*" * 50)
    print("Boat carries only the farmer + one item.\nRules: Fox eats Goat, Goat eats Cabbage if farmer not present.\n")

    for step, item in enumerate(path, 1):
        current = 0 if FARMER in banks[0] else 1
        other = 1 - current
        banks[current].remove(FARMER)
        banks[other].append(FARMER)
        if item:
            banks[current].remove(item)
            banks[other].append(item)
            print(f"Step {step}: Farmer takes {item} to the other bank.")
        else:
            print(f"Step {step}: Farmer crosses alone.")
        print(f"Left bank: {banks[0]}")
        print(f"Right bank: {banks[1]}")
        print("-" * 50)

    print("All items safely crossed! You win!")

# Start the automated game
run_game()
