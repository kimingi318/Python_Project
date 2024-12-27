#pig game
import random

def roll():
    min_value = 1
    max_value = 6
    roll = random.randint(min_value,max_value)

    return roll

# value = roll()
# print(value)

while True:
    players = input("Enter the number of players(2 - 4):  ")
    if players.isdigit():
        players = int(players)
        if 2 <= players <= 4:
            break
        else:
            print("The players should be atleast 2  and atmost 4")
    else:
        print("invalid input, try again")

# print(players)
max_score = 50
player_scores = [0 for _ in range(players)]

# print(player_scores)
while max(player_scores) < max_score:

    for player_idx in range(players):
        print("\nplayer number", player_idx + 1, "is your turn to roll .Good luck!")
        print("your total score is:",player_scores[player_idx],"\n")
        current_score = 0

        while True:
            should_roll = input("would you like to roll  (y)?  ")
            if should_roll.lower() != "y":
                break
            
            value = roll()
            if value == 1:
                current_score = 0
                player_scores[player_idx] = 0
                print("you rolled a 1! opps turn down and you scores are back to zero")
                break
            else:
                current_score += value
                print("you rolled a :",value)
                print("you score is now : ",current_score)

                
        player_scores[player_idx] += current_score
        print("your total score is : ",player_scores[player_idx])

max_score = max(player_scores)
min_score = min(player_scores)
winning_idx = player_scores.index(max_score)
loosing_idx = player_scores.index(min_score)
print("player number",winning_idx + 1, "is the winner with a score of:",max_score)
print("Congratulations!!")
print("player number",loosing_idx + 1, "is the looser with a score of:",min_score,"better luck next time")