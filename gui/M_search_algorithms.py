# M_search_algorithms.py
from collections import deque
import heapq
from gui.M_problem import GOAL_STATE, get_successors

def bfs(start):
    queue = deque([(start, [start])])
    visited = {start}  # Mark as visited when added to queue
    nodes_expanded = 0
    
    while queue:
        state, path = queue.popleft()
        nodes_expanded += 1
        
        if state == GOAL_STATE:
            return path, nodes_expanded
        
        for next_state in get_successors(state):
            if next_state not in visited:
                visited.add(next_state)  # Mark as visited immediately
                queue.append((next_state, path + [next_state]))
    
    return None, nodes_expanded

def dfs(start):
    stack = [(start, [start])]
    visited = {start}  # Mark as visited when added to stack
    nodes_expanded = 0
    
    while stack:
        state, path = stack.pop()
        nodes_expanded += 1
        
        if state == GOAL_STATE:
            return path, nodes_expanded
        
        for next_state in get_successors(state):
            if next_state not in visited:
                visited.add(next_state)  # Mark as visited immediately
                stack.append((next_state, path + [next_state]))
    
    return None, nodes_expanded

def heuristic(state):
    """Count items still on the left side (admissible heuristic)"""
    return sum(1 for item in state if item == "L")

def astar(start):
    # Priority queue: (f_score, counter, state, path, g_score)
    counter = 0  # Tiebreaker for heap
    pq = [(heuristic(start), counter, start, [start], 0)]
    visited = {}  # Maps state to best g_score seen
    nodes_expanded = 0
    
    while pq:
        f_score, _, state, path, g_score = heapq.heappop(pq)
        
        # Skip if we've found a better path to this state already
        if state in visited and visited[state] <= g_score:
            continue
        
        visited[state] = g_score
        nodes_expanded += 1
        
        if state == GOAL_STATE:
            return path, nodes_expanded
        
        for next_state in get_successors(state):
            new_g_score = g_score + 1
            
            # Only explore if we haven't seen this state or found a better path
            if next_state not in visited or new_g_score < visited[next_state]:
                counter += 1
                new_f_score = new_g_score + heuristic(next_state)
                heapq.heappush(pq, (new_f_score, counter, next_state, path + [next_state], new_g_score))
    
    return None, nodes_expanded# M_search_algorithms.py
from collections import deque
import heapq
from gui.M_problem import GOAL_STATE, get_successors

def bfs(start):
    queue = deque([(start, [start])])
    visited = {start}  # Mark as visited when added to queue
    nodes_expanded = 0
    
    while queue:
        state, path = queue.popleft()
        nodes_expanded += 1
        
        if state == GOAL_STATE:
            return path, nodes_expanded
        
        for next_state in get_successors(state):
            if next_state not in visited:
                visited.add(next_state)  # Mark as visited immediately
                queue.append((next_state, path + [next_state]))
    
    return None, nodes_expanded

def dfs(start):
    stack = [(start, [start])]
    visited = {start}  # Mark as visited when added to stack
    nodes_expanded = 0
    
    while stack:
        state, path = stack.pop()
        nodes_expanded += 1
        
        if state == GOAL_STATE:
            return path, nodes_expanded
        
        for next_state in get_successors(state):
            if next_state not in visited:
                visited.add(next_state)  # Mark as visited immediately
                stack.append((next_state, path + [next_state]))
    
    return None, nodes_expanded

def heuristic(state):
    """Count items still on the left side (admissible heuristic)"""
    return sum(1 for item in state if item == "L")

def astar(start):
    # Priority queue: (f_score, counter, state, path, g_score)
    counter = 0  # Tiebreaker for heap
    pq = [(heuristic(start), counter, start, [start], 0)]
    visited = {}  # Maps state to best g_score seen
    nodes_expanded = 0
    
    while pq:
        f_score, _, state, path, g_score = heapq.heappop(pq)
        
        # Skip if we've found a better path to this state already
        if state in visited and visited[state] <= g_score:
            continue
        
        visited[state] = g_score
        nodes_expanded += 1
        
        if state == GOAL_STATE:
            return path, nodes_expanded
        
        for next_state in get_successors(state):
            new_g_score = g_score + 1
            
            # Only explore if we haven't seen this state or found a better path
            if next_state not in visited or new_g_score < visited[next_state]:
                counter += 1
                new_f_score = new_g_score + heuristic(next_state)
                heapq.heappush(pq, (new_f_score, counter, next_state, path + [next_state], new_g_score))
    
    return None, nodes_expanded# M_search_algorithms.py
from collections import deque
import heapq
from gui.M_problem import GOAL_STATE, get_successors

def bfs(start):
    queue = deque([(start, [start])])
    visited = {start}  # Mark as visited when added to queue
    nodes_expanded = 0
    
    while queue:
        state, path = queue.popleft()
        nodes_expanded += 1
        
        if state == GOAL_STATE:
            return path, nodes_expanded
        
        for next_state in get_successors(state):
            if next_state not in visited:
                visited.add(next_state)  # Mark as visited immediately
                queue.append((next_state, path + [next_state]))
    
    return None, nodes_expanded

def dfs(start):
    stack = [(start, [start])]
    visited = {start}  # Mark as visited when added to stack
    nodes_expanded = 0
    
    while stack:
        state, path = stack.pop()
        nodes_expanded += 1
        
        if state == GOAL_STATE:
            return path, nodes_expanded
        
        for next_state in get_successors(state):
            if next_state not in visited:
                visited.add(next_state)  # Mark as visited immediately
                stack.append((next_state, path + [next_state]))
    
    return None, nodes_expanded

def heuristic(state):
    """Count items still on the left side (admissible heuristic)"""
    return sum(1 for item in state if item == "L")

def astar(start):
    # Priority queue: (f_score, counter, state, path, g_score)
    counter = 0  # Tiebreaker for heap
    pq = [(heuristic(start), counter, start, [start], 0)]
    visited = {}  # Maps state to best g_score seen
    nodes_expanded = 0
    
    while pq:
        f_score, _, state, path, g_score = heapq.heappop(pq)
        
        # Skip if we've found a better path to this state already
        if state in visited and visited[state] <= g_score:
            continue
        
        visited[state] = g_score
        nodes_expanded += 1
        
        if state == GOAL_STATE:
            return path, nodes_expanded
        
        for next_state in get_successors(state):
            new_g_score = g_score + 1
            
            # Only explore if we haven't seen this state or found a better path
            if next_state not in visited or new_g_score < visited[next_state]:
                counter += 1
                new_f_score = new_g_score + heuristic(next_state)
                heapq.heappush(pq, (new_f_score, counter, next_state, path + [next_state], new_g_score))
    
    return None, nodes_expanded