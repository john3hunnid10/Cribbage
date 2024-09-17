from deckObject import Card
from deckObject import Deck
import itertools

def main(hand: list[Card])->list[Card]:
    if(len(hand)!=6):
        raise Exception('Hand has too many cards')
    #creating the deck object, then removing the 6 cards in the hand
    deck=Deck()
    deck.removeCards(hand)
    #creating a list of all the 46 cards left in the deck
    deck.shuffle()
    flops=deck.deal(46)
    #creating a list of all 4 card combinations in a 6 card hand
    FourCardcombins,FourCardAvgs=[],[]
    FourCardcombins.extend(itertools.combinations(hand,4))
    #creating a list of all the average score of each hand
    for combins in FourCardcombins:
        combins=list(combins)
        FourCardAvgs.append(averagePoints(combins,flops))
    #getting the index of the highest scoring hand on average and returning the 4 card combination at that index
    MaxHand=FourCardcombins[FourCardAvgs.index(max(FourCardAvgs))]
    return MaxHand
    

    
    
    

def averagePoints(hand: list[Card], flops: list[Card])->int:
    #if the 4 card had is a flush, it will always be worth 4 points or more.
    #that is why check_flush returns 1, because when called later while checking a 5 card hand, a full flush is 5 points.
    #the reason the check is done before is because in cribbage you can only get a flush by having the 4 cards in your original hand.
    avgPoints=0
    #it gets the sum of all 46 possible 5 card hand combinations divides by 46 and returns that integer
    for flop in flops:
       avgPoints+=PointsCounter(hand+[flop])
    avgPoints=avgPoints/46
    if(check_flush(hand)==1):
        avgPoints+=4
    return avgPoints

def check_run(cards: list[Card])->int:
    #the rank order is stored, so that the hand can be sorted in rank order in order to form runs
    #the combination is sorted in rank order to make checking for runs easier
    rankAscending=sorted((cards),key=lambda card: card.order)
    runLength=1
    maxRunLength=0
    for i in range(len(rankAscending)-1):
        if cards[i].order+1==cards[i+1].order:
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


#example code: fill in how you see fit
# A=Ace, J=Jack, Q=Queen, K=King
# S=Spades, H=Hearts, D=Diamonds, C=Clubs
SCHand=[Card('5','S'),
      Card('6','H'),
      Card('J','C'),
      Card('10','D'),
      Card('4','C'),
      Card('A','D')
      ]
print("the best 4 card hand, given the input is:",main(SCHand))

#testing code
# FiChand1=[Card('5',5,'S'),
#       Card('K',10,'S'),
#       Card('J',10,'C'),
#       Card('10',10,'D'),
#       Card('5',5,'H')
#     ]
# FiChand2=[Card('5',5,'S'),
#       Card('6',6,'H'),
#       Card('J',10,'C'),
#       Card('10',10,'D'),
#       Card('4',4,'C')
#     ]
# FiChand3=[Card('4',4,'H'),
#        Card('2',2,'H'),
#        Card('K',10,'H'),
#        Card('9',9,'H'),
#        Card('A',1,'H')
#     ]

# FoChand1=[Card('5',5,'S'),
#       Card('K',10,'S'),
#       Card('J',10,'C'),
#       Card('10',10,'D'),
#     ]

# print("hand1 is:",PointsCounter(FiChand1))
# print("hand2 is:",PointsCounter(FiChand2))
# print("hand3 is:",PointsCounter(FiChand3)+4)
#deck=Deck()
#print(deck)
#deck.removeCards(FoChand1)
#print(deck)
#flops=deck.deal(46)
#print("average points for FoChand1 is: ",averagePoints(FourCardhand1,flops))
