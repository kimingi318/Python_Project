# FILE: /simple-python-game/simple-python-game/src/utils/__init__.py
def roll_dice():
    import random
    return random.randint(1, 6)

def calculate_score(current_score, rolled_value):
    if rolled_value == 1:
        return 0
    return current_score + rolled_value

def display_score(player_idx, score):
    print(f"Player {player_idx + 1}, your total score is: {score}")