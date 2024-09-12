from deckObject import Card, Deck
import itertools
def main(hand):
    return -1

def PointsCounter(hand):
    #this first creates each combination of 2+ cards to use to add up points
    combinations=[]
    for r in range(2, (len(hand)+1)):
        combinations.extend(itertools.extend.combinations(hand,r))
    