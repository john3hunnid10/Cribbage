This program takes a 6 card hand, and then returns the best 4 card hand.
To do this, it checks all possible "flip cards" that make a 5 card hand and return the 4 card hand that have the highest average points.
An input for a hand would be: 
main([Card('5',5,'S'),
Card('6',6,'H'),
Card('J',10,'C'),
Card('10',10,'D'),
Card('4',4,'C'),
Card('A',1,'D')])

This corresponds to a 6 card hand with
5 of Spades
6 of Hearts
Jack of Clubs
4 of Clubs
10 of Diamonds
where:A=Ace, J=Jack, Q=Queen, K=King and suits are: S=Spades, H=Hearts, D=Diamonds, C=Clubs
You can copy and paste this into the bottom as a template:              
InputHand=[Card('5',5,'S'),
Card('6',6,'H'),
Card('J',10,'C'),
Card('10',10,'D'),
Card('4',4,'C'),
Card('A',1,'D')]            
print("the best 4 card hand, given the input:",main(InputHand)
