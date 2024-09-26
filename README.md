Rules of Cribbage: https://en.wikipedia.org/wiki/Rules_of_cribbage

This program takes a 6 card hand in Cribbage, and then returns the best 4 card hand.
To do this, it checks all possible "flip cards" that make a 5 card hand and return the 4 card hand that have the highest average points.
For now, it doesn't ackoneldge that giving up 5 cards is bad, or to slightly prefer lower cards to get better chances at pegging, so it is not perfect.
It does its calculations based on average hand value.

An input for a hand would be: 
main([Card('5','S'),
Card('6','H'),
Card('J','C'),
Card('10','D'),
Card('4','C'),
Card('A','D')])

This corresponds to a 6 card hand with:
5 of Spades,
6 of Hearts,
Jack of Clubs,
10 of Diamonds,
4 of Clubs,
Ace of Diamonds. 


Where A=Ace, J=Jack, Q=Queen, K=King and suits are: S=Spades, H=Hearts, D=Diamonds, C=Clubs

You can copy and paste this into the bottom as a template:              
```InputHand=[Card('5','S'),
Card('6','H'),
Card('J','C'),
Card('10','D'),
Card('4','C'),
Card('A','D')] print("the best 4 card hand, given the input:",main(InputHand))`

OUTPUT: the best 4 card hand, given the input is: (5 of Spades, 6 of Hearts, J of Clubs, 4 of Clubs)
