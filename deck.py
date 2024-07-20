from card import Card
import random
class Deck:
    value = {"Two":2,"Three":3,"Four":4,"Five":5,"Six":6,"Seven":7,"Eight":8,"Nine":9,"Ten":10,"Jack":11,"Queen":12,"King":13,"Ace":14}
    suit = ("Diamond","Clubs","Heart","Spades")
    rank = ("Two","Three","Four","Five","Six","Seven","Eight","Nine","Ten","Jack","Queen","King","Ace") 
    def __init__(self):    
        self.all_cards = []
        for suits in Deck.suit:
            for ranks in Deck.rank :
                created_card = Card(suits,ranks)
                self.all_cards.append(created_card)
    def shuffle(self):
      random.shuffle(self.all_cards)
    def deal_one(self):
        return self.all_cards.pop()
    