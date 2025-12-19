# main.py

import time
from gui.M_problem import INITIAL_STATE
from gui.M_search_algorithms import bfs, dfs, astar

algorithms = {
    "BFS": bfs,
    "DFS": dfs,
    "A*": astar
}

for name, algo in algorithms.items():
    print(f"\n--- {name} ---")
    start_time = time.time()

    path, nodes = algo(INITIAL_STATE)

    end_time = time.time()

    print("Solution Path:")
    for step in path:
        print(step)

    print(f"Path Length: {len(path)-1}")
    print(f"Nodes Expanded: {nodes}")
    print(f"Time: {end_time - start_time:.6f} seconds")
