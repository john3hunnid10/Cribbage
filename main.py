from deckObject import Card, Deck
import itertools
def main(hand):
    return -1

def PointsCounter(hand: list[Card]) -> int:
    #this first creates each combination of 2+ cards to use to add up points
    #the rank order is stored, so that the hand can be sorted in rank order in order to form runs
    rank_order={'A':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'10':10,'J':11,'Q':12,'K':13}
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
        #the combination is sorted in rank order to make checking for runs easier
        if(len>3):
            rankAscending=sorted(combins,key=lambda card: rank_order[card.rank])
            if(len==3):
                if(rank_order[combins[0].rank]+1==rank_order[combins[1].rank] and rank_order[combins[1].rank]+1==rank_order[combins[2].rank]):
                    runs+=[combins[0],combins[1],combins[2]]
            #run of 5 is also easy to check            
            if(len==4):
                rankAscending=sorted(combins,key=lambda card: rank_order[card.rank])
            if(len==5):
                if(rank_order[combins[0].rank]+1==rank_order[combins[1].rank]):
                    if(rank_order[combins[1].rank]+1==rank_order[combins[2].rank]):
                        if(rank_order[combins[2].rank]+1==rank_order[combins[3].rank]):
                            if(rank_order[combins[3].rank]+1==rank_order[combins[4].rank]):
                                runs+=[combins[0],combins[1],combins[2],combins[3],combins[4]]



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