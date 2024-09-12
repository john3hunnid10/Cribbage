#deck Object
import random


#card class
class Card:
    def __init__(self,rank,value,suit):
        self.suit=suit
        self.rank=rank
        self.value=value
    #print function for testing
    def __repr__(self):
        return f"{self.rank} of {self.suit} (Value: {self.value})"

class Deck:
    #available suits H=hearts, D=diamonds, C=clubs, S=spades 
    suits=['H','D','C','S']
    #rankValTuple has each rank of card and its corresponding value
    rankValTuple=[
        ('A',1),('2',2),('3',3),('4',4),('5',5),('6',6),('7',7),
        ('8',8),('9',9),('10',10),('J',10),('Q',10),('K',10)]
    #The deck is constructed with every combination of suit & rank, and the value is added to card object as well
    def __init__(self):
        self.cards=[Card(rank,value,suit) for rank,value in self.rankValTuple for suit in self.suits]
    
    #shuffles the deck
    def shuffle(self):
        random.shuffle(self.cards)

    #shows how many cards are left
    def __len__(self):
        return len(self.cards)
    
    #Note: always shuffle before deal 
    def deal(self, numCards):
        if(numCards>len(self.cards)):
            return -1
        hand=self.cards[:numCards]
        self.cards=self.cards[numCards:]
        return hand
    #the deal returned is a list of Card Objects