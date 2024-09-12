from deckObject import Card, Deck
import itertools
def main(hand):
    return -1

def PointsCounter(hand) -> int:
    #this first creates each combination of 2+ cards to use to add up points
    combinations=[]
    points=0
    for r in range(2, (len(hand)+1)):
        combinations.extend(itertools.combinations(hand,r))
    for combins in combinations:
        #checking for cards adding up to 15
        sumOfHand=sum(card.value for card in combins)
        if(sumOfHand==15):
            points+=2
        #testing for pairs and since pair royal is 6 (the three pairs that can be made), points are only added as pairs
        if(len(combins))==2:
            if(combins[0].rank==combins[1].rank):
                points+=2



hand1=[Card('5',5,'S'),
      Card('K',10,'S'),
      Card('J',10,'C'),
      Card('10',10,'D'),
      Card('5',5,'H')
      ]
combinations1=PointsCounter(hand1)
for combins in combinations1:
    if(len(combins))==2:
        print(combins[0].rank,combins[1].rank)