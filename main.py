from deckObject import Card, Deck
import itertools
def main(hand):
    return -1

def PointsCounter(hand):
    #this first creates each combination of 2+ cards to use to add up points
    combinations=[]
    for r in range(2, (len(hand)+1)):
        combinations.extend(itertools.extend.combinations(hand,r))
    return combinations


hand1=[Card('5',5,'S'),
      Card('K',10,'S'),
      Card('J',10,'C'),
      Card('10',10,'D'),
      Card('5',5,'H')
      ]
combinations1=PointsCounter(hand1)
print(combinations1)