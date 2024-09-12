#deck Object
import random


#card class
class Card:
    def __init__(self,suit,rank,value):
        self.suit=suit
        self.rank=rank
        self.value=value

class Deck:
    suits=['H','D','C','S']
    rankValTuple=[
        ('A',1),('2',2),('3',3),('4',4),('5',5),('6',6),('7',7),
        ('8',8),('9',9),('10',10),('J',10),('Q',10),('K',10)]
    def __init__(self):
        self.cards=[Card(suit,rank,value) for suit in self.suits for rank,value in self.rankValTuple]
    