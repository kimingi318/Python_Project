#a game that mimics the card game ..four players are involved and the player who matches the last card with the card in the deck wins
#card with number 2 or 3 on it makes the next player to pick two or three cards from the deck 
#only an A card can block the pick two or pick three cards
#the black and the red joker cards makes the next player to pick 5 cards from the deck
#the special A card can block the black and red joker cards
#8 and Q cards are question cards and the player who picks them is asked a question and if they fail to answer the question they pick two cards from the deck
#j cards are the skip cards and the next player is skipped
#k cards are the reverse cards and the direction of the game is reversed
#same card numbers are used to change the color of the game
#has 54 cards in the deck 
import random


players = input("Enter the number of players ,atleast 3: ")
if players.isdigit():
            players = int(players)
else:
    print("invalid input, try again")
            
if players < 3:
                    print("The players should be atleast 3 enter valid number please")
else:
                    print("\n Game On!!!!!\n")
                   
                    cards_deck = []

                    def pick():
                        def cardNo():
                            min_value = 2
                            max_value = 10
                            cardshape = ["hearts", "diamonds", "clubs", "spades"]
                            return random.randint(min_value, max_value), random.choice(cardshape)

                        def specialCard():
                            specialCard = ["A", "J", "Q", "K"]
                            cardshape = ["hearts", "diamonds", "clubs", "spades"]
                            return random.choice(specialCard), random.choice(cardshape)

                        def jokerCard():
                            jokerCard = ["black joker", "red joker"]
                            return random.choice(jokerCard)

                        while True:
                            choice = random.choice([1, 2, 3])
                            if choice == 1:
                                card = cardNo()
                            elif choice == 2:
                                card = specialCard()
                            else:
                                card = jokerCard()
                            
                            if card not in cards_deck:
                                cards_deck.append(card)
                                return card
                            
                            

                    starting_card = pick()
                    while starting_card == "black joker" or starting_card == "red joker":
                        starting_card = pick()
                    
                    if (starting_card[0] == "A" or 
                         starting_card[0] == "J" or 
                         starting_card[0] == "Q" or 
                         starting_card[0] == "K" or 
                         starting_card[0] == 8 or 
                         starting_card[0] == 3 or 
                         starting_card[0] == 2):
                        starting_card = pick()
                    else:
                        print("\nThe starting card is:\n ",starting_card)
                        players_cards = [[pick() for _ in range(3)] for _ in range(players)]
                        

                        while True:
                            for player_idx in range(players):
                                print("\nplayer number", player_idx + 1, "your initial card area : ", players_cards[player_idx])

                                while True:
                                    value = input("pick a card from the deck(y):  ")
                                    if value.lower() == "y":
                                        picked = pick()
                                        print("\nyou picked \n", picked)
                                        players_cards[player_idx].append(picked)
                                        print("\nyour new card are : ", players_cards[player_idx])
                                        print("\nstarting card is: ", starting_card)
                                        break

                                    else:
                                        print("You can only drop a card that either matches the shape or has the same number as the starting card")
                                        dropped = input("Do you want to drop a card(y)?  ")
                                        while dropped.lower() != "y":
                                            print("its either you drop or pick a card")
                                            break

                                        else:
                                            card = input("which card do you want to drop?  ")
                                            crd = int(card) - 1

                                            popped_card = players_cards[player_idx].pop(crd)
                                            print("\nyou dropped card number\n", popped_card)
                                            print("\nyour new cards are: \n", players_cards[player_idx])
                                            starting_card = popped_card
                                            print("\nstarting card is: ", starting_card)
                                            

                                            if popped_card[0] == 2:
                                                next_player_idx = (player_idx + 1) % players
                                                card_shape = popped_card[1]
                                                print("player number", next_player_idx + 1, "you have to pick two cards from the deck\n You can only avoid this by dropping an A card\n,a 2 card or a 3 card with the same shape\n")
                                                print("\nplayer number", next_player_idx + 1, "your initial card area : ", players_cards[next_player_idx])
                                                A_card = input("Do you have any of the cards to drop(y)?  ")
                                                if A_card.lower() == "y":
                                                    card_index = input("Drop the  card number:  ")
                                                    card_index = int(card_index) - 1
                                                    card_to_drop = players_cards[next_player_idx][card_index]
                                                    if (card_to_drop[0] == "A" or card_to_drop[0] == 2 or (card_to_drop[0] == 3 and card_to_drop[1] == card_shape)):
                                                        players_cards[next_player_idx].pop(card_index)
                                                        print("you have successfully avoided picking two cards\n")
                                                        
                                                        break
                                                    else:
                                                        for _ in range(2):
                                                            picked = pick()
                                                            players_cards[next_player_idx].append(picked)
                                                            print("player number", next_player_idx + 1, "new cards are : ", players_cards[next_player_idx])
                                                            continue
                                                else:
                                                    for _ in range(2):
                                                            picked = pick()
                                                            players_cards[next_player_idx].append(picked)
                                                            print("player number", next_player_idx + 1, "new cards are : ", players_cards[next_player_idx])
                                                            continue


                                            elif popped_card[0] == 3:
                                                next_player_idx = (player_idx + 1) % players
                                                card_shape = popped_card[1]
                                                print("player number", next_player_idx + 1, "you have to pick three cards from the deck\n You can only avoid this by dropping an A ,a 3 pr a 2 card of the same shape")
                                                print("\nplayer number", next_player_idx + 1, "your initial card area : ", players_cards[next_player_idx])
                                                A_card = input("Do you have any of cards to drop(y)?  ")
                                                if A_card.lower() == "y":
                                                    card_index = input("Drop the card number:  ")
                                                    card_index = int(card_index) - 1
                                                    card_to_drop = players_cards[next_player_idx][card_index]
                                                    if ( card_to_drop[0] == "A" or  card_to_drop[0] == 3 or ( card_to_drop[0] == 2 and  card_to_drop[1] == card_shape)):
                                                        players_cards[next_player_idx].pop(card_index)
                                                        print("you have successfully avoided picking three cards")
                                                        break
                                                    else:
                                                        for _ in range(3):
                                                            picked = pick()
                                                            players_cards[next_player_idx].append(picked)
                                                            print("player number", next_player_idx + 1, "new cards are : ", players_cards[next_player_idx])
                                                            continue
                                                else:
                                                    for _ in range(3):
                                                            picked = pick()
                                                            players_cards[next_player_idx].append(picked)
                                                            print("player number", next_player_idx + 1, "new cards are : ", players_cards[next_player_idx])
                                                            continue


                                            elif popped_card in ["black joker", "red joker"]:
                                                next_player_idx = (player_idx + 1) % players
                                                print("player number", next_player_idx + 1, "you have to pick five cards from the deck\n You can only avoid this by dropping a special A card(A spades)\n or  2 a cards\n")
                                                print("\nplayer number", next_player_idx + 1, "your initial card area : ", players_cards[next_player_idx])
                                                A_card = input("Do you have a special A card or 2 A cards to drop(y)? \n ")
                                                if A_card.lower() == "y":
                                                    popped_card = input("Drop the respective  card number:  ")
                                                    card_index = int(popped_card) - 1
                                                    card_to_drop = players_cards[next_player_idx][card_index]
                                                    if card_to_drop[0] == "A" and card_to_drop[1] == "spades":
                                                        popped_card = players_cards[next_player_idx].pop(card_index)
                                                        print("you have successfully avoided picking five cards")
                                                        break
                                                    else:
                                                        for _ in range(5):
                                                            picked = pick()
                                                            players_cards[next_player_idx].append(picked)
                                                            print("player number", next_player_idx + 1, "new cards are : ", players_cards[next_player_idx])
                                                            continue
                                                else:
                                                    for _ in range(5):
                                                        picked = pick()
                                                        players_cards[next_player_idx].append(picked)
                                                        print("player number", next_player_idx + 1, "new cards are : ", players_cards[next_player_idx])
                                                        continue
                                            
                                            elif popped_card[0] == 8 or popped_card[0] == "Q":
                                                print("player number", player_idx + 1, "You've dropped question card,either drop or pick an answer card\n")
                                                print("player number", player_idx + 1, "your initial card area : ", players_cards[player_idx])
                                                Answer = input("\nDo you have an Answer card to drop(y)?  ")
                                                if Answer.lower() == "y":
                                                    card_index = input("Drop the Answer card number:  ")
                                                    popped_card = int(card_index) - 1
                                                    card_to_drop = players_cards[player_idx][popped_card]
                                                    while card_to_drop[0] == 'Q' or card_to_drop[0] == 8:
                                                        print("\nYou've dropped a question card. Provide or pick the answer\n")
                                                        players_cards[player_idx].pop(card_index)
                                                        Answer = input("Do you have an Answer card to drop(y)?  ")
                                                        if Answer.lower() == "y":
                                                            card_index = input("Drop the Answer card number:  ")
                                                            card_index = int(card_index) - 1
                                                            card_to_drop = players_cards[player_idx][card_index]
                                                            if card_to_drop[1] == popped_card[1]:
                                                              players_cards[player_idx].pop(card_index)
                                                              print("You have successfully dropped an answer card")
                                                              break
                                                            else:
                                                                picked = pick()
                                                                players_cards[player_idx].append(picked)
                                                                print("player number", player_idx + 1, "new cards are : ", players_cards[player_idx])
                                                                break
                                                        else:
                                                            picked = pick()
                                                            players_cards[player_idx].append(picked)
                                                            print("Card", picked, "has been added to your deck")
                                                            print("Player number", player_idx + 1, "new cards are: ", players_cards[player_idx])
                                                            break
                                                    
                                                else:
                                                    picked = pick()
                                                    players_cards[player_idx].append(picked)
                                                    print("card",picked, "has been added to your deck")
                                                    print("player number", player_idx + 1, "new cards are : ", players_cards[player_idx])
                                                    break


                                            # elif popped_card[0] == "J":
                                            #     player_idx = (player_idx + 1) % players
                                            #     print("player number", player_idx + 1, "you have been skipped\n")
                                            #     continue
                                                
                                            
                                            # elif popped_card[0] == "K":
                                            #     print("The direction of the game has been reversed\n")
                                            #     players_cards.reverse()
                                            #     player_idx = players - player_idx - 1
                                            #     break
                                            break
