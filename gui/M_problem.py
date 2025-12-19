# M_problem.py

from typing import Tuple

State = Tuple[str, str, str, str]  # (Farmer, Fox, Goat, Cabbage)
LEFT = "L"
RIGHT = "R"

INITIAL_STATE = (LEFT, LEFT, LEFT, LEFT)
GOAL_STATE = (RIGHT, RIGHT, RIGHT, RIGHT)
def is_safe(state: State) -> bool:
    farmer, fox, goat, cabbage = state

    # Fox eats goat
    if fox == goat and farmer != fox:
        return False

    # Goat eats cabbage
    if goat == cabbage and farmer != goat:
        return False

    return True
def get_successors(state: State):
    successors = []
    farmer, fox, goat, cabbage = state

    def move(item_index=None):
        new_state = list(state)
        new_state[0] = RIGHT if farmer == LEFT else LEFT

        if item_index is not None:
            if state[item_index] == farmer:
                new_state[item_index] = new_state[0]
            else:
                return None

        return tuple(new_state)

    for i in [None, 1, 2, 3]:  # alone, fox, goat, cabbage
        new_state = move(i)
        if new_state and is_safe(new_state):
            successors.append(new_state)

    return successors
