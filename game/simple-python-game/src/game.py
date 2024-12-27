def roll():
    import random
    return random.randint(1, 6)

def main():
    print("Welcome to the Simple Python Game!")
    players = input("Enter the number of players (2 - 4): ")
    
    while not players.isdigit() or not (2 <= int(players) <= 4):
        print("Invalid input. Please enter a number between 2 and 4.")
        players = input("Enter the number of players (2 - 4): ")
    
    players = int(players)
    player_scores = [0] * players
    max_score = 50

    while max(player_scores) < max_score:
        for player_idx in range(players):
            print(f"\nPlayer {player_idx + 1}, it's your turn!")
            current_score = 0
            
            while True:
                should_roll = input("Would you like to roll (y)? ")
                if should_roll.lower() != 'y':
                    break
                
                value = roll()
                if value == 1:
                    current_score = 0
                    print("You rolled a 1! Your turn is over and your score resets to zero.")
                    break
                else:
                    current_score += value
                    print(f"You rolled: {value}. Your current score is: {current_score}.")
            
            player_scores[player_idx] += current_score
            print(f"Player {player_idx + 1}'s total score: {player_scores[player_idx]}")

    max_score = max(player_scores)
    winning_idx = player_scores.index(max_score)
    print(f"Player {winning_idx + 1} wins with a score of: {max_score}!")

if __name__ == "__main__":
    main()