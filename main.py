from deckObject import Card, Deck
import itertools
rank_order={'A':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'10':10,'J':11,'Q':12,'K':13}
def main(hand):
    return -1

def check_run(cards: list[Card])->int:
    #the combination is sorted in rank order to make checking for runs easier
    rankAscending=sorted(combins,key=lambda card: rank_order[card.rank])
    runLength=0
    for i in range(len(rankAscending) - 1):
        if rank_order[rankAscending[i].rank]+1!=rank_order[rankAscending[i+1].rank]:
            return 0
        runLength+=1
    if(runLength<3):
        return 0
    return (runLength)


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