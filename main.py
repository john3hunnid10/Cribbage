from deckObject import Card, Deck
import itertools
#the rank order is stored, so that the hand can be sorted in rank order in order to form runs
rank_order={'A':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'10':10,'J':11,'Q':12,'K':13}
def main(hand):
    deck=Deck()
    #TODO: remove the 6 cards passed in by the hand
    #making a list of all 4 card combinations in a 6 card hand
    deck.shuffle()
    flops=deck.deal(46)
    FourCardcombins=[]
    FourCardcombins.extend(itertools.combinations(hand,4))
    FourCardAvgs=[]
    for combins in FourCardcombins:
        FourCardAvgs.append(averagePoints(combins,flops))
    MaxHandIndex=FourCardAvgs.index(max(FourCardAvgs))
    MaxHand=FourCardcombins[MaxHandIndex]
    return MaxHand
    

    
    
    

def averagePoints(hand,flops):
    #if the 4 card had is a flush, it will always be worth 4 points or more.
    #that is why check_flush returns 1, because when called later while checking a 5 card hand, a full flush is 5 points.
    #the reason the check is done before is because in cribbage you can only get a flush by having the 4 cards in your original hand.
    if(check_flush(hand)==1):
        avgPoints=4
    else:
        avgPoints
    avgPoints+=sum([PointsCounter(hand+[flopCard]) for flopCard in flops])/46
    return avgPoints

def check_run(cards: list[Card])->int:
    #the combination is sorted in rank order to make checking for runs easier
    rankAscending=sorted((cards),key=lambda card: rank_order[card.rank])
    runLength=1
    maxRunLength=0
    for i in range(len(rankAscending)-1):
        if rank_order[rankAscending[i].rank]+1==rank_order[rankAscending[i+1].rank]:
            runLength+=1
        elif (runLength>=3):
            maxRunLength=max(maxRunLength,runLength)
        runLength=1
    if(runLength>=3):
        maxRunLength=max(maxRunLength,runLength)
    return maxRunLength
def check_flush(cards: list[Card])->int:
    #since a 4 card flush can only be awarded if the 4 cards are in the original hand, the points will be added to the value before the flop
    #therefore when it is a 5 card flush it is only worth 1 more point so that is why 5 points aren't being added
    for i in range(len(cards)-1):
        if(cards[i].suit!=cards[i+1].suit):
            return 0
    return 1


def PointsCounter(hand: list[Card]) -> int:
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
        #testing for pairs and since pair royal is 6 (the three pairs that can be made), points are only added as pairs not 3 of a kind
        if(len(combins))==2:
            if(combins[0].rank==combins[1].rank):
                points+=2
       #in order to prevent redundancy, runs and flushes are only checked when the whole hand is being observed 
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
      Card('4',4,'C')
    ]
hand3=[Card('4',4,'H'),
       Card('2',2,'H'),
       Card('K',10,'H'),
       Card('9',9,'H'),
       Card('A',1,'H')
    ]

FourCardhand1=[Card('5',5,'S'),
      Card('K',10,'S'),
      Card('J',10,'C'),
      Card('10',10,'D'),
    ]
print("hand1 is:",PointsCounter(hand1))
print("hand2 is:",PointsCounter(hand2))
print("hand3 is:",PointsCounter(hand3)+4)
print("average points for FourCardHand1 is:",main(FourCardhand1))