from card import Card 
from deck import Deck 
from player import Player

Player1 = Player("Shivangi")
Player2 = Player("Astha")
New_Deck = Deck()
New_Deck.shuffle()
for x in range(26):
       Player1.add_card(New_Deck.deal_one())
       Player2.add_card(New_Deck.deal_one())
       
game_on = True
round_no = 0
while game_on:

    round_no += 1
    print(f"Round{ round_no}")
    
    if len(Player1.all_cards) == 0:
        print(f"Ohh no!! {Player1.name} ran out of cards")
        print(f"{Player2.name} won the game ")
        game_on= False 
        break
        
    if len(Player2.all_cards) == 0:
        print(f"Ohh no!! {Player2.name} ran out of cards")
        print(f"{Player1.name} won the game ")
        game_on= False 
        break
        
    player_one_card = []
    player_one_card.append(Player1.remove_one())
    
    player_two_card = []
    player_two_card.append(Player2.remove_one())

    at_war= True
    
    while at_war:
        if player_one_card[-1].value > player_two_card[-1].value :
            Player1.add_card(player_one_card[-1])
            Player1.add_card(player_two_card[-1])

            at_war = False
            
        elif player_one_card[-1].value < player_two_card[-1].value :
              Player2.add_card(player_one_card[-1])
              Player2.add_card(player_two_card[-1])

              at_war = False
        else :
            print("WAR!!!!!")
            
            if len(Player1.all_cards) < 5:
                print(f"Oh no! {Player1.name} cannot go on with the war")
                print(f"{Player2.name} won the game ")
                game_on = False
                break 
            
            elif len(Player2.all_cards) < 5:
                print(f"Oh no! {Player2.name} cannot go on with the war")
                print(f"{Player1.name} won the game ")
                game_on = False
                break 

            else:
                for i in range(5):
                    player_one_card.append(Player1.remove_one())
                    player_two_card.append(Player2.remove_one())
                     