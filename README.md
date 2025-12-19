# Farmer–Fox–Goat–Cabbage Puzzle

## 1. Introduction

The **Farmer–Fox–Goat–Cabbage** problem is a classic Artificial Intelligence (AI) puzzle used to demonstrate **state-space representation**, **constraints**, and **search algorithms**.  
The challenge is to safely transport all entities across a river while respecting specific rules that restrict certain entities from being left alone together.

This project applies:

- Intelligent agent concepts
    
- PEAS modeling
    
- Problem formulation
    
- Search algorithms (BFS, DFS, UCS)
    
- Solution visualization

---

## 2. Intelligent Agent Description

### Agent Type

**Goal-Based Intelligent Agent**

### Agent Role

The agent controls the **farmer**, deciding which action to take at each step to move all entities safely from the left bank to the right bank.

### Interaction with Environment

- The agent **perceives** the position of all entities.
    
- The agent **acts** by rowing the boat alone or with one item.
    
- The agent **plans** a sequence of actions using search algorithms.

---

## 3. PEAS Model

### Performance Measure

- Successfully transport **Farmer, Fox, Goat, and Cabbage** to the **right bank**
    
- **Avoid unsafe states**:
    
    - Fox alone with Goat
        
    - Goat alone with Cabbage
        
- **Minimize number of river crossings**

---

### Environment

- **Type**: Discrete, deterministic, static, fully observable
    
- **Components**:
    
    - Two riverbanks (Left, Right)
        
    - One boat
        
    - Four entities (Farmer, Fox, Goat, Cabbage)
        
- **Constraints**:
    
    - Boat carries only the farmer and **one item**
        
    - Farmer must be present to row the boat

---

### Actuators

The agent can perform the following actions:

- Move farmer alone
    
- Move farmer with fox
    
- Move farmer with goat
    
- Move farmer with cabbage

---

### Sensors

The agent can observe:

- Position of the farmer (left/right)
    
- Position of the fox, goat, cabbage
    
- Whether a move results in a valid or dangerous state
    
- Whether the goal state is reached

---

## 4. Problem Formulation

### State Representation

Each state is represented as a **4-tuple**:

```
(F, X, G, C)
```

Where:

- `0` = Left bank
    
- `1` = Right bank
    

|Variable|Meaning|
|---|---|
|F|Farmer|
|X|Fox|
|G|Goat|
|C|Cabbage|

---

### Initial State

```
(0, 0, 0, 0)
```

All entities start on the **left bank**.

---

### Goal State

```
(1, 1, 1, 1)
```

All entities safely reach the **right bank**.

---

### State Space

- Total possible states: `2⁴ = 16`
    
- Many states are **invalid** due to safety constraints.
    

---

### Valid State Constraints

A state is **invalid** if:

- Fox and Goat are together **without Farmer**
    
- Goat and Cabbage are together **without Farmer**
    

---

### Operators / Actions (Successor Function)

|Action|Condition|State Transition|
|---|---|---|
|Farmer alone|Always|`(F, X, G, C) → (1−F, X, G, C)`|
|Farmer + Fox|F = X|`(F, X, G, C) → (1−F, 1−X, G, C)`|
|Farmer + Goat|F = G|`(F, X, G, C) → (1−F, X, 1−G, C)`|
|Farmer + Cabbage|F = C|`(F, X, G, C) → (1−F, X, G, 1−C)`|

---

### Goal Test

Check if:

```
state == (1, 1, 1, 1)
```

---

### Path Cost

- Each river crossing costs **1**
    
- Total cost = number of crossings  
    (Search aims to minimize this cost)
    

---

## 5. Search Algorithms Used

### 1. Breadth-First Search (BFS)

- Explores states level by level
    
- **Guarantees shortest solution**
    
- Higher memory usage
    

### 2. Depth-First Search (DFS)

- Explores deeply before backtracking
    
- Lower memory usage
    
- May find non-optimal solutions
    

### 3. Uniform Cost Search (UCS) 

- Expands lowest-cost node first
    
- Guarantees optimal solution 

---

## 6. Optimal Solution Path (Example)

Minimum crossings = **7**

|Step|Action|
|---|---|
|1|Farmer takes Goat to right|
|2|Farmer returns alone|
|3|Farmer takes Fox to right|
|4|Farmer brings Goat back|
|5|Farmer takes Cabbage to right|
|6|Farmer returns alone|
|7|Farmer takes Goat to right|

Goal reached safely 

---

## 7. Results Comparison

| Algorithm | Solution Found | Nodes Expanded | Optimal        | Time   |
| --------- | -------------- | -------------- | -------------- | ------ |
| BFS       | Yes            | High           | Yes            | Medium |
| DFS       | Yes            | Low            | Not guaranteed | Fast   |
| UCS       | Yes            | Medium         | Yes            | Medium |

---

## 8. Interface / Demo

- Console-based visualization:
    
    - Displays current state after each move
        
    - Shows chosen action
        
- Optional GUI:
    
    - Tkinter riverbanks visualization
        
    - Step-by-step animation of crossings

---

## 9. Conclusion

This project demonstrates how classical AI problems can be solved using:

- Intelligent agent design
    
- PEAS modeling
    
- State-space formulation
    
- Search algorithms
    

The **Farmer–Fox–Goat–Cabbage puzzle** effectively illustrates:

- Constraint satisfaction
    
- Optimal search
    
- Agent reasoning in deterministic environments
    

---

