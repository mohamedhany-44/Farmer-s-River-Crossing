from collections import deque

def is_valid_state(state):
    """Check if a state is valid (no one gets eaten)"""
    farmer, fox, goat, cabbage = state
    
    # If goat and fox are alone (farmer not with them)
    if goat == fox and goat != farmer:
        return False
    
    # If goat and cabbage are alone (farmer not with them)
    if goat == cabbage and goat != farmer:
        return False
    
    return True

def get_next_states(state):
    """Generate all possible next states from current state"""
    farmer, fox, goat, cabbage = state
    next_states = []
    new_farmer = 1 - farmer  # Farmer crosses (0->1 or 1->0)
    
    # Farmer goes alone
    new_state = (new_farmer, fox, goat, cabbage)
    if is_valid_state(new_state):
        next_states.append(new_state)
    
    # Farmer takes fox
    if fox == farmer:
        new_state = (new_farmer, new_farmer, goat, cabbage)
        if is_valid_state(new_state):
            next_states.append(new_state)
    
    # Farmer takes goat
    if goat == farmer:
        new_state = (new_farmer, fox, new_farmer, cabbage)
        if is_valid_state(new_state):
            next_states.append(new_state)
    
    # Farmer takes cabbage
    if cabbage == farmer:
        new_state = (new_farmer, fox, goat, new_farmer)
        if is_valid_state(new_state):
            next_states.append(new_state)
    
    return next_states

def bfs_solve():
    """Solve using Breadth-First Search"""
    initial_state = (0, 0, 0, 0)  # All on left bank
    goal_state = (1, 1, 1, 1)      # All on right bank
    
    # Queue stores: (current_state, path)
    queue = deque([(initial_state, [initial_state])])
    visited = {initial_state}
    
    while queue:
        current_state, path = queue.popleft()
        
        # Check if we reached the goal
        if current_state == goal_state:
            return path
        
        # Explore next states
        for next_state in get_next_states(current_state):
            if next_state not in visited:
                visited.add(next_state)
                queue.append((next_state, path + [next_state]))
    
    return None  # No solution found

def print_solution(path):
    """Print the solution in a readable format"""
    if not path:
        print("No solution found!")
        return
    
    labels = ['Farmer', 'Fox', 'Goat', 'Cabbage']
    
    print("BFS Solution:")
    print("=" * 50)
    for i, state in enumerate(path):
        left = [labels[j] for j in range(4) if state[j] == 0]
        right = [labels[j] for j in range(4) if state[j] == 1]
        
        print(f"Step {i}:")
        print(f"  Left bank:  {', '.join(left) if left else 'Empty'}")
        print(f"  Right bank: {', '.join(right) if right else 'Empty'}")
        print()
    
    print(f"Total steps: {len(path) - 1}")

# Run the algorithm
if __name__ == "__main__":
    solution = bfs_solve()
    print_solution(solution)