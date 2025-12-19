# Game characters
FARMER = "farmer"
FOX = "fox"
GOAT = "goat"
CABBAGE = "cabbage"

ALL_ITEMS = [FARMER, FOX, GOAT, CABBAGE]

# banks[0] -> left bank, banks[1] -> right bank
banks = [ALL_ITEMS.copy(), []]


# ---------------- GAME CHECKS ----------------

def has_won():
    return sorted(banks[1]) == sorted(ALL_ITEMS)


def has_lost():
    for bank in banks:
        if FARMER not in bank:
            if FOX in bank and GOAT in bank:
                print("\nThe fox ate the goat.\n")
                return True
            if GOAT in bank and CABBAGE in bank:
                print("\nThe goat ate the cabbage.\n")
                return True
    return False


# ---------------- HELPERS ----------------

def farmer_bank():
    """Return index of the bank where the farmer is"""
    return 0 if FARMER in banks[0] else 1


def show_banks():
    for i, bank in enumerate(banks):
        bank.sort()
        print(", ".join(f"{idx}. {item}" for idx, item in enumerate(bank)))
        if i == 0:
            print("~" * 50)


# ---------------- MOVE LOGIC ----------------

def move(item=None):
    current = farmer_bank()
    other = 1 - current

    # Move farmer
    banks[other].append(FARMER)
    banks[current].remove(FARMER)

    # Move item if chosen
    if item and item in banks[current]:
        banks[other].append(item)
        banks[current].remove(item)
        print(f"The farmer and the {item} crossed the river.")
    else:
        print("The farmer crossed alone.")

    show_banks()

    if has_lost():
        print("Game Over!")
        return True

    if has_won():
        print("You Win!")
        return True

    return False


# ---------------- PLAYER TURN ----------------

def play():
    while True:
        print("\n")
        print("*" * 50)
        print("Choose item number to move with farmer (or Q to quit):")
        print("\n")
        show_banks()

        choice = input(">>> ").strip()

        if choice.upper() == "Q":
            print("Goodbye!")
            return

        location = farmer_bank()

        if choice.isdigit():
            index = int(choice)
            if index < len(banks[location]):
                if move(banks[location][index]):
                    return


# ---------------- START GAME ----------------

print("*" * 50)
print("Farmer, Fox, Goat, and cabbage")
print("*" * 50)

print("""
Boat carries only the farmer + one item.
Rules:
- Fox eats Goat without farmer
- Goat eats cabbage without farmer
""")

play()
