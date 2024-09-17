#deck Object
import random


#card class
class Card:
    rank_order={'A':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'10':10,'J':11,'Q':12,'K':13}
    def __init__(self,rank:str,suit:str):
        #check inputs,
        #if suit or rank is lowercase it gets turned uppercase
        if (suit not in ('S','H','D','C')):
            if(suit.upper() in ('S','H','D','C')):
                suit=suit.upper()
            else:
                raise Exception('Invalid Suit')
        if(rank not in self.rank_order):
            if(rank.upper() in ('A','J','Q','K')):
                rank=rank.upper()
            else:
                raise Exception('Invalid rank')
        #If you're keeping track through versions you'll notice I removed value as an input and instead added it in construction
        #this was to make it more user friendly so now an input is Card('5','S') instead of Card('5',5,'S')
        self.suit=suit
        self.rank=rank
        if(rank in ('J','Q','K')):
            self.value=10
        else:
            self.value=self.rank_order[rank]
        self.order=self.rank_order[rank]
    #print function for testing
    def __repr__(self):
        str_rank={'S':"Spades",'H':"Hearts",'D':"Diamonds",'C':"Clubs"}
        return f"{self.rank} of {str_rank[self.suit]}"
    #equal function for removal of cards
    def __eq__(self, other):
        return self.rank==other.rank and self.suit==other.suit

class Deck:
    #available suits H=hearts, D=diamonds, C=clubs, S=spades 
    suits=['H','D','C','S']
    #ranks has each rank of card 
    ranks=['A','2','3','4','5','6','7','8','9','10','J','Q','K']
    #The deck is constructed with every combination of suit rank
    def __init__(self):
        self.cards=[Card(rank,suit) for rank in self.ranks for suit in self.suits]
    #shuffles the deck
    def shuffle(self):
        random.shuffle(self.cards)

    #shows how many cards are left
    def __len__(self):
        return len(self.cards)
    #print the deck for testing
    def __repr__(self):
        return f"Deck with {len(self.cards)} cards left"
    def deal(self, numCards:int):
        hand=self.cards[:numCards]
        self.cards=self.cards[numCards:]
        return hand
    #the deal returned is a list of Card Objects

    #removal function, it loops through the deck and takes out the specified cards
    def removeCards(self, hand: list[Card]):
        for card in hand:
            if card in self.cards:
                self.cards.remove(card)