from deckObject import Card, Deck
import itertools
rank_order={'A':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'10':10,'J':11,'Q':12,'K':13}
def main(hand):
    return -1

def check_run(cards: list[Card])->int:
    #the combination is sorted in rank order to make checking for runs easier
    rankAscending=sorted((cards),key=lambda card: rank_order[card.rank])
    runLength=0
    for i in range(len(rankAscending) - 1):
        if rank_order[rankAscending[i].rank]+1!=rank_order[rankAscending[i+1].rank]:
            runLength=1
        runLength+=1
    if(runLength>=3):
        return (runLength)
    else:
        return (runLength)
def check_flush(cards: list[Card])->int:
    #since a 4 card flush can only be awarded if the 4 cards are in the original hand, the points will be added to the value before the flop
    #therefore when it is a 5 card flush it is only worth 1 more point so that is why 5 points aren't being added
    for i in range(len(cards)):
        if(cards[i].suit!=cards[i+1].suit):
            return 0
    return 1


def PointsCounter(hand: list[Card]) -> int:
    #this first creates each combination of 2+ cards to use to add up points
    #the rank order is stored, so that the hand can be sorted in rank order in order to form runs
    
    combinations=[]
    points=0
    runs=[]
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
        #if the observed combination has 3 or more cards, its viable for a run
        if(len(combins)==5):
            points+=check_run(combins)
            points+=check_flush(combins)
    return points



hand1=[Card('5',5,'S'),
      Card('K',10,'S'),
      Card('J',10,'C'),
      Card('10',10,'D'),
      Card('5',5,'H')
    ]
hand2=[Card('5',5,'S'),
      Card('6',6,'H'),
      Card('J',10,'C'),
      Card('10',10,'D'),
      Card('4',4,'C')]
print("hand1 is:",PointsCounter(hand1))
print("hand2 is:",PointsCounter(hand2))
