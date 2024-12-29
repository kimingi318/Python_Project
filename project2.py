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
            
while True:
                if players < 3:
                    print("The players should be atleast 3 enter valid number please")
                else:
                    print("\n Game On!!!!!\n")
                    def pick():
                            def cardNo():
                                min_value = 2
                                max_value = 10
                                cardshape = ["hearts","diamonds","clubs","spades"]
                                return random.randint(min_value,max_value) , random.choice(cardshape)
                            
                            def specialCard():
                                specialCard = ["A","J","Q","K"]
                                cardshape = ["hearts","diamonds","clubs","spades"]
                                return random.choice(specialCard) ,random.choice(cardshape)
                            
                            card_number = cardNo() 
                            special_card = specialCard()
                            
                            if random.choice([True,False]):
                                return card_number
                            else:
                                return special_card
                            
                            

                    starting_card = pick()
                    print("\nthe starting card is:\n ",starting_card)
                    players_cards = [[pick() for _ in range(3)] for _ in range(players)]
                    # print("\nthe initial cards for the players are:\n",players_cards)
                    for player_idx in range(players):
                        print("your initial card area : ",players_cards[player_idx])
                        value = input("pick a card from the deck(y):  ")
                        if value.lower() == "y":
                          picked = pick()
                          print("\nyou picked \n",picked)
                          players_cards[player_idx].append(picked)
                          print("your new card are : ",players_cards[player_idx])
                          break

                        else:
                              dropped = input("do you want to drop a card(y)?  ")
                              while dropped.lower() != "y":
                                  print("its either you drop or pick a card")
                                  break

                              else:
                                  card = input("which card do you want to drop?  ")
                                  if card in players_cards[player_idx]:
                                      players_cards[player_idx].remove(card)
                                      break
                                  else:
                                      print("you dont have that card in your deck")
                                      break

