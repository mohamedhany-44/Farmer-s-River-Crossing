"""
Comparative Analysis of Search Algorithms
for Farmer-Fox-Goat-Cabbage Puzzle
"""

import time
from collections import deque
import heapq

class PuzzleSolver:
    def __init__(self):
        self.start = (0, 0, 0, 0)
        self.goal = (1, 1, 1, 1)
        self.nodes_expanded = 0
    
    def is_valid(self, state):
        F, X, G, C = state
        if X == G and F != X:
            return False
        if G == C and F != G:
            return False
        return True
    
    def get_successors(self, state):
        F, X, G, C = state
        moves = []
        
        # Farmer alone
        new_state = (1 - F, X, G, C)
        if self.is_valid(new_state):
            moves.append((new_state, "Farmer alone", 1))
        
        # Farmer with Fox
        if F == X:
            new_state = (1 - F, 1 - X, G, C)
            if self.is_valid(new_state):
                moves.append((new_state, "Farmer + Fox", 1))
        
        # Farmer with Goat
        if F == G:
            new_state = (1 - F, X, 1 - G, C)
            if self.is_valid(new_state):
                moves.append((new_state, "Farmer + Goat", 1))
        
        # Farmer with Cabbage
        if F == C:
            new_state = (1 - F, X, G, 1 - C)
            if self.is_valid(new_state):
                moves.append((new_state, "Farmer + Cabbage", 1))
        
        return moves
    
    def bfs(self):
        """Breadth-First Search"""
        self.nodes_expanded = 0
        visited = set()
        queue = deque()
        queue.append((self.start, [], []))
        
        while queue:
            state, path, moves = queue.popleft()
            self.nodes_expanded += 1
            
            if state in visited:
                continue
            visited.add(state)
            
            if state == self.goal:
                return path + [state], moves, self.nodes_expanded
            
            for next_state, move_desc, cost in self.get_successors(state):
                if next_state not in visited:
                    queue.append((next_state, path + [state], moves + [move_desc]))
        
        return None, None, self.nodes_expanded
    
    def dfs(self):
        """Depth-First Search"""
        self.nodes_expanded = 0
        visited = set()
        stack = [(self.start, [], [])]
        
        while stack:
            state, path, moves = stack.pop()
            self.nodes_expanded += 1
            
            if state in visited:
                continue
            visited.add(state)
            
            if state == self.goal:
                return path + [state], moves, self.nodes_expanded
            
            for next_state, move_desc, cost in self.get_successors(state):
                if next_state not in visited:
                    stack.append((next_state, path + [state], moves + [move_desc]))
        
        return None, None, self.nodes_expanded
    
    def ucs(self):
        """Uniform Cost Search"""
        self.nodes_expanded = 0
        visited = set()
        pq = [(0, self.start, [], [])]  # (cost, state, path, moves)
        
        while pq:
            cost, state, path, moves = heapq.heappop(pq)
            self.nodes_expanded += 1
            
            if state in visited:
                continue
            visited.add(state)
            
            if state == self.goal:
                return path + [state], moves, self.nodes_expanded, cost
            
            for next_state, move_desc, move_cost in self.get_successors(state):
                if next_state not in visited:
                    heapq.heappush(pq, (cost + move_cost, next_state, 
                                      path + [state], moves + [move_desc]))
        
        return None, None, self.nodes_expanded, float('inf')
    
    def dls(self, limit=10):
        """Depth-Limited Search"""
        self.nodes_expanded = 0
        
        def dls_recursive(state, depth, path, moves, visited):
            self.nodes_expanded += 1
            
            if state == self.goal:
                return path + [state], moves
            
            if depth == 0:
                return None, None
            
            visited.add(state)
            
            for next_state, move_desc, cost in self.get_successors(state):
                if next_state not in visited:
                    result_path, result_moves = dls_recursive(
                        next_state, depth - 1, 
                        path + [state], moves + [move_desc], 
                        visited.copy()
                    )
                    if result_path:
                        return result_path, result_moves
            
            return None, None
        
        return dls_recursive(self.start, limit, [], [], set())
    
    def ids(self):
        """Iterative Deepening Search"""
        self.nodes_expanded = 0
        depth = 0
        
        while True:
            path, moves = self.dls(depth)
            if path:
                return path, moves, self.nodes_expanded, depth
            depth += 1
            if depth > 20:  # Safety limit
                return None, None, self.nodes_expanded, depth

def compare_algorithms():
    solver = PuzzleSolver()
    results = []
    
    print("=" * 80)
    print("COMPARATIVE ANALYSIS OF SEARCH ALGORITHMS")
    print("=" * 80)
    
    # BFS
    start_time = time.time()
    bfs_path, bfs_moves, bfs_nodes = solver.bfs()
    bfs_time = time.time() - start_time
    
    # DFS
    start_time = time.time()
    dfs_path, dfs_moves, dfs_nodes = solver.dfs()
    dfs_time = time.time() - start_time
    
    # UCS
    start_time = time.time()
    ucs_path, ucs_moves, ucs_nodes, ucs_cost = solver.ucs()
    ucs_time = time.time() - start_time
    
    # IDS
    start_time = time.time()
    ids_path, ids_moves, ids_nodes, ids_depth = solver.ids()
    ids_time = time.time() - start_time
    
    # Display results
    print("\n" + "=" * 80)
    print("PERFORMANCE METRICS")
    print("=" * 80)
    
    data = [
        ("Algorithm", "Solution Length", "Nodes Expanded", "Time (s)", "Optimal"),
        ("BFS", len(bfs_path)-1 if bfs_path else "N/A", bfs_nodes, f"{bfs_time:.6f}", "✓" if bfs_path else "✗"),
        ("DFS", len(dfs_path)-1 if dfs_path else "N/A", dfs_nodes, f"{dfs_time:.6f}", "?" if dfs_path else "✗"),
        ("UCS", len(ucs_path)-1 if ucs_path else "N/A", ucs_nodes, f"{ucs_time:.6f}", "✓" if ucs_path else "✗"),
        ("IDS", len(ids_path)-1 if ids_path else "N/A", ids_nodes, f"{ids_time:.6f}", "✓" if ids_path else "✗"),
    ]
    
    # Print table
    for row in data:
        print(f"{row[0]:<10} | {str(row[1]):<15} | {str(row[2]):<15} | {row[3]:<12} | {row[4]:<8}")
    
    print("\n" + "=" * 80)
    print("ANALYSIS")
    print("=" * 80)
    
    print("\n1. COMPLETENESS:")
    print("   - BFS: Complete (finds solution if it exists)")
    print("   - DFS: Not complete (may get stuck in infinite loops)")
    print("   - UCS: Complete")
    print("   - IDS: Complete")
    
    print("\n2. OPTIMALITY:")
    print("   - BFS: Optimal (finds shortest path)")
    print("   - DFS: Not optimal")
    print("   - UCS: Optimal (finds minimum cost path)")
    print("   - IDS: Optimal when cost=1 per step")
    
    print("\n3. TIME COMPLEXITY:")
    print(f"   - BFS: O(b^d) = exponential in depth")
    print(f"   - DFS: O(b^m) = exponential in maximum depth")
    print(f"   - UCS: O(b^(C*/ε)) where C* is optimal cost")
    print(f"   - IDS: O(b^d) = same as BFS")
    
    print("\n4. SPACE COMPLEXITY:")
    print("   - BFS: O(b^d) = stores all nodes in frontier")
    print("   - DFS: O(bm) = linear in maximum depth")
    print("   - UCS: O(b^(C*/ε))")
    print("   - IDS: O(bd) = linear in depth")
    
    print("\n5. BEST FOR THIS PROBLEM:")
    print("   - BFS or UCS for optimal solution")
    print("   - DFS for memory efficiency")
    print("   - IDS for balance between optimality and memory")
    
    # Save results to file
    with open("algorithm_comparison.txt", "w") as f:
        f.write("Algorithm Comparison Results\n")
        f.write("=" * 50 + "\n")
        for row in data:
            f.write(f"{row[0]:<10} | {str(row[1]):<15} | {str(row[2]):<15} | {row[3]:<12} | {row[4]:<8}\n")
    
    print("\nResults saved to 'algorithm_comparison.txt'")

if __name__ == "__main__":
    compare_algorithms()