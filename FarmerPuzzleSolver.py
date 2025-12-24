import time
from collections import deque
import heapq

class FarmerPuzzleSolver:
    """Intelligent agent for solving the Farmer-Fox-Goat-Cabbage puzzle"""
    
    def __init__(self):
        # State representation: (Farmer, Fox, Goat, Cabbage)
        # 0 = Left bank, 1 = Right bank
        self.start_state = (0, 0, 0, 0)  # All on left bank
        self.goal_state = (1, 1, 1, 1)   # All on right bank
        self.items = ["Farmer", "Fox", "Goat", "Cabbage"]
        self.nodes_expanded = 0
    
    def is_valid_state(self, state):
        """Check if state is safe according to constraints"""
        F, X, G, C = state
        
        # Fox and Goat together without Farmer
        if X == G and F != X:
            return False
        
        # Goat and Cabbage together without Farmer
        if G == C and F != G:
            return False
        
        return True
    
    def get_successors(self, state):
        """Generate all possible next states from current state"""
        F, X, G, C = state
        successors = []
        
        # Farmer moves alone
        new_state = (1 - F, X, G, C)
        if self.is_valid_state(new_state):
            successors.append((new_state, "Farmer alone"))
        
        # Farmer moves with Fox (only if Fox is on same bank)
        if F == X:
            new_state = (1 - F, 1 - X, G, C)
            if self.is_valid_state(new_state):
                successors.append((new_state, "Farmer takes Fox"))
        
        # Farmer moves with Goat (only if Goat is on same bank)
        if F == G:
            new_state = (1 - F, X, 1 - G, C)
            if self.is_valid_state(new_state):
                successors.append((new_state, "Farmer takes Goat"))
        
        # Farmer moves with Cabbage (only if Cabbage is on same bank)
        if F == C:
            new_state = (1 - F, X, G, 1 - C)
            if self.is_valid_state(new_state):
                successors.append((new_state, "Farmer takes Cabbage"))
        
        return successors
    
    def print_state(self, state):
        """Display the current state visually"""
        left_bank = []
        right_bank = []
        
        for i, item in enumerate(self.items):
            if state[i] == 0:
                left_bank.append(item)
            else:
                right_bank.append(item)
        
        print(f"Left Bank:  {', '.join(left_bank) if left_bank else 'Empty'}")
        print(f"Right Bank: {', '.join(right_bank) if right_bank else 'Empty'}")
        print("-" * 40)
    
    def print_solution(self, path, moves, algorithm_name):
        """Display the complete solution with steps"""
        print(f"\n{'='*60}")
        print(f"{algorithm_name} SOLUTION")
        print(f"{'='*60}")
        
        for i, state in enumerate(path):
            if i == 0:
                print(f"\nStep 0: Initial State")
            else:
                print(f"\nStep {i}: {moves[i-1]}")
            
            self.print_state(state)
        
        print(f"\nTotal steps: {len(path) - 1}")
        print(f"Nodes expanded: {self.nodes_expanded}")
        print(f"{'='*60}")
    
    def bfs(self):
        """Breadth-First Search - Guarantees shortest path"""
        self.nodes_expanded = 0
        visited = set()
        queue = deque()
        
        # Store (state, path, moves)
        queue.append((self.start_state, [self.start_state], []))
        
        while queue:
            state, path, moves = queue.popleft()
            self.nodes_expanded += 1
            
            if state in visited:
                continue
            visited.add(state)
            
            if state == self.goal_state:
                return path, moves
            
            for next_state, move_desc in self.get_successors(state):
                if next_state not in visited:
                    queue.append((next_state, 
                                 path + [next_state], 
                                 moves + [move_desc]))
        
        return None, None
    
    def dfs(self):
        """Depth-First Search - Memory efficient"""
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
        
        self.nodes_expanded = 0
        visited = set()
        stack = []
        
        # Store (state, path, moves)
        stack.append((self.start_state, [self.start_state], []))
        
        while stack:
            state, path, moves = stack.pop()
            self.nodes_expanded += 1
            
            if state in visited:
                continue
            visited.add(state)
            
            if state == self.goal_state:
                return path, moves
            
            for next_state in get_next_states(state):
                if next_state not in visited:
                    move_desc = self._get_move_description(state, next_state)
                    stack.append((next_state, 
                                 path + [next_state], 
                                 moves + [move_desc]))
        
        return None, None
    
    def _get_move_description(self, old_state, new_state):
        """Helper function to describe the move"""
        F_old, X_old, G_old, C_old = old_state
        F_new, X_new, G_new, C_new = new_state
        
        if X_old != X_new:
            return "Farmer takes Fox"
        elif G_old != G_new:
            return "Farmer takes Goat"
        elif C_old != C_new:
            return "Farmer takes Cabbage"
        else:
            return "Farmer alone"
    
    def ucs(self):
        """Uniform Cost Search - Optimal cost solution"""
        self.nodes_expanded = 0
        visited = set()
        
        # Priority queue: (cost, state, path, moves)
        pq = [(0, self.start_state, [self.start_state], [])]
        heapq.heapify(pq)
        
        while pq:
            cost, state, path, moves = heapq.heappop(pq)
            self.nodes_expanded += 1
            
            if state in visited:
                continue
            visited.add(state)
            
            if state == self.goal_state:
                return path, moves, cost
            
            for next_state, move_desc in self.get_successors(state):
                if next_state not in visited:
                    # Each move costs 1
                    heapq.heappush(pq, (cost + 1, next_state, 
                                       path + [next_state], 
                                       moves + [move_desc]))
        
        return None, None, float('inf')
    
    def compare_algorithms(self):
        """Compare all three algorithms"""
        print("\n" + "="*80)
        print("FARMER-FOX-GOAT-CABBAGE PUZZLE - ALGORITHM COMPARISON")
        print("="*80)
        
        results = []
        
        # BFS
        print("\n1. BREADTH-FIRST SEARCH (BFS)")
        print("-" * 40)
        start_time = time.time()
        bfs_path, bfs_moves = self.bfs()
        bfs_time = time.time() - start_time
        
        if bfs_path:
            print(f"✓ Solution found in {len(bfs_path)-1} steps")
            print(f"  Nodes expanded: {self.nodes_expanded}")
            print(f"  Time taken: {bfs_time:.6f} seconds")
            results.append(("BFS", len(bfs_path)-1, self.nodes_expanded, bfs_time, "Yes"))
        else:
            print("✗ No solution found")
            results.append(("BFS", "N/A", self.nodes_expanded, bfs_time, "No"))
        
        # DFS
        print("\n2. DEPTH-FIRST SEARCH (DFS)")
        print("-" * 40)
        start_time = time.time()
        dfs_path, dfs_moves = self.dfs()
        dfs_time = time.time() - start_time
        
        if dfs_path:
            print(f"✓ Solution found in {len(dfs_path)-1} steps")
            print(f"  Nodes expanded: {self.nodes_expanded}")
            print(f"  Time taken: {dfs_time:.6f} seconds")
            results.append(("DFS", len(dfs_path)-1, self.nodes_expanded, dfs_time, "Yes"))
        else:
            print("✗ No solution found")
            results.append(("DFS", "N/A", self.nodes_expanded, dfs_time, "No"))
        
        # UCS
        print("\n3. UNIFORM COST SEARCH (UCS)")
        print("-" * 40)
        start_time = time.time()
        ucs_path, ucs_moves, ucs_cost = self.ucs()
        ucs_time = time.time() - start_time
        
        if ucs_path:
            print(f"✓ Solution found in {len(ucs_path)-1} steps (cost: {ucs_cost})")
            print(f"  Nodes expanded: {self.nodes_expanded}")
            print(f"  Time taken: {ucs_time:.6f} seconds")
            results.append(("UCS", len(ucs_path)-1, self.nodes_expanded, ucs_time, "Yes"))
        else:
            print("✗ No solution found")
            results.append(("UCS", "N/A", self.nodes_expanded, ucs_time, "No"))
        
        # Display comparison table
        print("\n" + "="*80)
        print("COMPARISON SUMMARY")
        print("="*80)
        print(f"{'Algorithm':<12} {'Steps':<10} {'Nodes':<12} {'Time (s)':<12} {'Solution':<10}")
        print("-" * 60)
        
        for algo, steps, nodes, time_taken, solution in results:
            time_str = f"{time_taken:.6f}" if isinstance(time_taken, float) else str(time_taken)
            print(f"{algo:<12} {steps:<10} {nodes:<12} {time_str:<12} {solution:<10}")
        
        # Analysis
        print("\n" + "="*80)
        print("ANALYSIS")
        print("="*80)
        print("\nCompleteness:")
        print("  - BFS: Complete (always finds solution if exists)")
        print("  - DFS: Complete (with state checking)")
        print("  - UCS: Complete (always finds solution if exists)")
        
        print("\nOptimality:")
        print("  - BFS: Optimal (finds shortest path)")
        print("  - DFS: Not optimal (may find longer path)")
        print("  - UCS: Optimal (finds minimum cost path)")
        
        print("\nBest for this problem:")
        print("  - For optimal solution: BFS or UCS")
        print("  - For memory efficiency: DFS")
        print("  - All algorithms successfully solve the puzzle")


def main():
    """Main function to run the puzzle solver"""
    print("="*80)
    print("INTELLIGENT AGENT: FARMER-FOX-GOAT-CABBAGE PUZZLE SOLVER")
    print("="*80)
    print("\nProblem Description:")
    print("- The farmer needs to transport a fox, goat, and cabbage across a river.")
    print("- The boat can carry only the farmer and one item at a time.")
    print("- Constraints:")
    print("  1. Fox cannot be left alone with Goat (fox eats goat)")
    print("  2. Goat cannot be left alone with Cabbage (goat eats cabbage)")
    print("- Goal: Get all to the right bank safely.")
    
    solver = FarmerPuzzleSolver()
    
    while True:
        print("\n" + "="*80)
        print("MAIN MENU")
        print("="*80)
        print("1. Run Breadth-First Search (BFS)")
        print("2. Run Depth-First Search (DFS)")
        print("3. Run Uniform Cost Search (UCS)")
        print("4. Compare All Algorithms")
        print("5. Exit")
        
        choice = input("\nEnter your choice (1-5): ").strip()
        
        if choice == "1":
            print("\nRunning BFS...")
            path, moves = solver.bfs()
            if path:
                solver.print_solution(path, moves, "BREADTH-FIRST SEARCH")
            else:
                print("No solution found!")
        
        elif choice == "2":
            print("\nRunning DFS...")
            path, moves = solver.dfs()
            if path:
                solver.print_solution(path, moves, "DEPTH-FIRST SEARCH")
            else:
                print("No solution found!")
        
        elif choice == "3":
            print("\nRunning UCS...")
            path, moves, cost = solver.ucs()
            if path:
                solver.print_solution(path, moves, "UNIFORM COST SEARCH")
                print(f"Total cost: {cost}")
            else:
                print("No solution found!")
        
        elif choice == "4":
            solver.compare_algorithms()
        
        elif choice == "5":
            print("\nThank you for using the puzzle solver. Goodbye!")
            break
        
        else:
            print("\nInvalid choice. Please enter a number between 1 and 5.")
        
        input("\nPress Enter to continue...")


if __name__ == "__main__":
    main()