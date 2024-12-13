# Everything, including comments,  should fit on a single line in a reasonable editor.
# Historically that's 80 characters. Now it shouldn't be more than like 100. You linter
# should handle this for you. Also your non-pythonic spacing

# https://github.com/psf/black

# delete this. I know that
#imports

# I'm anal about the way imports should be written.
# These sections w/ line breaks

# built-ins in alphebetical order
import itertools

# external packages in alphabetical order

# local packages in alphabetical order

# in python we use snake_case not camelCase so it should be deck_object
# however, that's not an object, it's a class (actually a module containing a class)
# from deck_object import DeckObject
# I'd do from deck_models import Card, Deck
from deckObject import Card, Deck


# Code says what it does, comments say _why_. There should not be many comments
# Ideally, I would never read your code unless I was trying to copy it or modify it
# If you want to explain the algorithm it goes in the docstring.

def main(hand: list[Card]) -> list[Card]:
    '''Takes in a 6 card hand input and returns the 4 card hand with the highest average points

    This is the main function that takes in a 6 card hand input and returns the 4 card hand
    with the highest average points.

    We create a new deck, remove the input hand, and create a list of the remaining cards.
    Then we create a list of all 4 card combinations in a 6 card hand, as well as their
    averages. ...

    Args:
        those

    Returns:
        these

    Raises:
        Also

    '''
    #checking that the hand is 6 card hand
    for card in hand:
        if type(card) != Card:
            raise ValueError("not all cards are a card object")
    if (len(hand) != 6):
        raise ValueError('Hand has too many cards')

    deck=Deck()
    deck.removeCards(hand)
    deck.shuffle()
    flops=deck.deal(46)
    FourCardcombins,FourCardAvgs=[],[]
    FourCardcombins.extend(itertools.combinations(hand,4))
    for combins in FourCardcombins:
        FourCardAvgs.append(averagePoints(combins,flops))
    MaxHand=FourCardcombins[FourCardAvgs.index(max(FourCardAvgs))]
    return MaxHand

#this function takes an input of the 4 hand, and the 46 possible draws from the deck
# it returns the average points of the hand
def averagePoints(hand: list[Card], flops: list[Card])->int:
    #if the 4 card had is a flush, it will always be worth 4 points or more.
    #that is why check_flush returns 1, because when called later while checking a 5 card hand, a full flush is 5 points.
    #the reason the check is done before is because in cribbage you can only get a flush by having the 4 cards in your original hand.
    #for testing purposes hand gets typecast to a list
    hand=list(hand)
    avgPoints=0
    #it gets the sum of all 46 possible 5 card hand combinations divides by 46 and returns that integer
    for flop in flops:
       #the flop card gets added to the
       hand.append(flop)
       avgPoints+=(PointsCounter(hand))
       hand.pop()
    avgPoints=avgPoints/46
    if(check_flush):
        avgPoints+=4
    return avgPoints

#this function takes in a 5 card hand input, and returns the length of the run given that the run is longer than 3
def check_run(cards: list[Card])->int:
    #the rank order is stored, so that the hand can be sorted in rank order in order to form runs
    #the combination is sorted in rank order to make checking for runs easier
    rankAscending=sorted((cards),key=lambda card: card.order)
    runLength=1
    maxRunLength=1
    for i in range(len(rankAscending)-1):
        if rankAscending[i].order+1==rankAscending[i+1].order:
            runLength+=1
        else:
            maxRunLength=max(maxRunLength,runLength)
            runLength=1

    if(maxRunLength>=3):
        maxRunLength=max(maxRunLength,runLength)
    else:
        return 0
    return maxRunLength

#this function takes in a 4 or 5 card hand and returns true if all cards are the same suit and false if not
def check_flush(cards: list[Card])->bool:
    #since a 4 card flush can only be awarded if the 4 cards are in the original hand, the points will be added to the value before the flop
    #therefore when it is a 5 card flush it is only worth 1 more point so that is why 5 points aren't being added
    for i in range(len(cards)-1):
        if(cards[i].suit!=cards[i+1].suit):
            return False
    return True

#this function takes in a 5 card hand and returns how many points its worth the points for 4 card flush are added after
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
            if(check_flush(hand)):
                points+=1
    return points


# How is this intended to be called? I would personally use
# https://click.palletsprojects.com/en/stable/ to make this a command line executable
# that takes the path to a json blob that describes the hand
